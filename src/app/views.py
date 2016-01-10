from flask import render_template, flash, redirect, session, url_for, request, g, Response
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm, EditProfileForm, BookmarksEditForm, SearchForm, PostsEditForm, ContactForm
from .models import User, Bookmark, Post
from .emails import send_email_contact
from .oauth import OAuthSignIn
from datetime import datetime
import json
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

@app.route('/')
@app.route('/index')
def index():
    posts = []
    return render_template('index.html',
                           title='Home',
                           user=g.user,
                           posts=posts)


@app.route('/api/comments', methods=['GET', 'POST'])
def comments_handler():

    with open(os.path.join(APP_STATIC, 'comments.json'), 'r') as file:
        comments = json.loads(file.read())

    if request.method == 'POST':
        comments.append(request.form.to_dict())

        with open('comments.json', 'w') as file:
            file.write(json.dumps(comments, indent=4, separators=(',', ': ')))

    return Response(json.dumps(comments), mimetype='application/json', headers={'Cache-Control': 'no-cache'})


@app.route('/about')
def about():
    return render_template('about.html',
                           title='About',
                           menu='about',
                           user=g.user)


@app.route('/user')
@login_required
def user():
    return render_template('user.html',
                           user=g.user,
                           menu='profile')


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()
        g.search_form = SearchForm()
    #g.locale = get_locale()


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           menu='login',
                           form=form)


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(nickname=username,
                    email=email,
                    social_id=social_id,
                    is_banned=False,
                    is_admin=True,
                    timestamp=datetime.utcnow())
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        sender = form.mail_from.data
        message = form.message.data
        send_email_contact(sender, message)
        flash('Your email has been sent.', 'info')
        return redirect(url_for('index'))
    else:
        form.mail_from.data = ''
        form.message.data = ''
    return render_template('contact.html', form=form)


@app.route('/user/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit_profile.html', form=form)


@app.route('/bookmarks')
@login_required
def bookmarks():
    links = Bookmark.query.filter(Bookmark.user_id==g.user.id).all()
    tags = []
    for link in links:
        tagline = link.tags
        tagline = tagline.replace(', ', ',')
        arrtag = tagline.split(',')
        if arrtag:
            for t in arrtag:
                if t not in tags:
                    tags.append(t)

    return render_template('bookmarks.html',
                           user=g.user,
                           links=links,
                           menu='bookmarks',
                           tags=tags)

@app.route('/bookmarks/list/<tag>')
@login_required
def bookmarks_list(tag=None):
    links = Bookmark.query.all()
    tags = []
    for link in links:
        tagline = link.tags
        tagline = tagline.replace(', ', ',')
        arrtag = tagline.split(',')
        if arrtag:
            for t in arrtag:
                if t not in tags:
                    tags.append(t)

    if tag:
        pattern = "%%%s%%" % tag
        #pattern = "%news%"
        links = Bookmark.query.filter(Bookmark.tags.like(pattern)).all()

    return render_template('bookmarks.html',
                           user=g.user,
                           links=links,
                           menu='bookmarks',
                           tags=tags)


@app.route('/bookmarks/edit/<id>', methods=['GET', 'POST'])
@login_required
def bookmarks_edit(id):
    model = Bookmark.load(id)
    if model:
        form = BookmarksEditForm()
        if form.validate_on_submit():
            # POST
            model.name = form.name.data
            model.url = form.url.data.lower()
            model.tags = form.tags.data.lower()
            db.session.add(model)
            db.session.commit()
            flash('Your changes have been saved.')
            return redirect(url_for('bookmarks'))
        else:
            # GET
            form.name.data = model.name
            form.url.data = model.url
            form.tags.data = model.tags
        return render_template('bookmarks_edit.html', form=form)
    else:
        # not found
        flash('Bookmark not found.')
        return redirect(url_for('bookmarks_list'))


@app.route('/bookmarks/new', methods=['GET', 'POST'])
@login_required
def bookmarks_new():
    form = BookmarksEditForm()
    if form.validate_on_submit():
        # POST
        model = Bookmark()
        model.user_id = g.user.id
        model.name = form.name.data
        model.url = form.url.data.lower()
        model.tags = form.tags.data.lower()
        model.timestamp = datetime.utcnow()
        db.session.add(model)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('bookmarks'))
    else:
        # GET
        form.name.data = ''
        form.url.data = ''
        form.tags.data = ''
    return render_template('bookmarks_edit.html', form=form)


@app.route('/')
@app.route('/posts')
def posts_list():
    posts = Post.query.all()
    return render_template('posts_list.html',
                           title='Posts',
                           user=g.user,
                           menu='notes',
                           posts=posts)


@app.route('/post/<id>', methods=['GET'])
@login_required
def post(id):
    post = Post.load(id)
    if post:
        return render_template('post.html', post=post)
    else:
        flash('Post was not found.')
        return redirect(url_for('posts_list'))


@app.route('/posts/new', methods=['GET', 'POST'])
@login_required
def posts_new():
    form = PostsEditForm()
    if form.validate_on_submit():
        # POST
        model = Post()
        model.user_id = g.user.id
        model.title = form.title.data
        model.body = form.body.data
        model.tags = form.tags.data.lower()
        model.timestamp = datetime.utcnow()
        db.session.add(model)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('posts_list'))
    else:
        # GET
        form.title.data = ''
        form.body.data = ''
        form.tags.data = ''
    return render_template('posts_edit.html', form=form)


@app.route('/posts/edit/<id>', methods=['GET', 'POST'])
@login_required
def posts_edit(id):
    model = Post.load(id)
    if model:
        form = PostsEditForm()
        if form.validate_on_submit():
            # POST
            if form.delete.data:
                # delete
                db.session.delete(model)
                db.session.commit()
                flash('The record was deleted.')
            else:
                # save
                model.title = form.title.data
                model.body = form.body.data
                model.tags = form.tags.data.lower()
                db.session.add(model)
                db.session.commit()
                flash('Your changes have been saved.')
            return redirect(url_for('posts_list'))
        else:
            # GET
            form.title.data = model.title
            form.body.data = model.body
            form.tags.data = model.tags
        return render_template('posts_edit.html', form=form)
    else:
        # not found
        flash('Post not found.')
        return redirect(url_for('posts_list'))


@app.route('/search', methods=['POST'])
@login_required
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('search_results', query=g.search_form.search.data))


@app.route('/search_results/<query>')
@login_required
def search_results(query):
    results = Post.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
    return render_template('search_results.html',
                           query=query,
                           results=results)


# ------------------------
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500