from app import db, lm
from hashlib import md5

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    social_id = db.Column(db.String(64), index=True, unique=True)
    is_banned = db.Column(db.Boolean(), default=False)
    is_admin = db.Column(db.Boolean(), default=False)
    timestamp = db.Column(db.DateTime)
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    bookmarks = db.relationship('Bookmark', backref='owner', lazy='dynamic')

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    @lm.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @staticmethod
    def make_unique_nickname(nickname):
        new_nickname = nickname
        if User.query.filter_by(nickname=nickname).first() is None:
            return new_nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname=new_nickname).first() is None:
                break
            version += 1
        return new_nickname

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.String(8000))
    tags = db.Column(db.String(250))
    is_public = db.Column(db.Boolean(), default=False)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @staticmethod
    def load(bid):
        return Post.query.get(int(bid))

    def __repr__(self):
        return '<Post %r>' % (self.body)


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    url = db.Column(db.String(140))
    tags = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @staticmethod
    def load(bid):
        return Bookmark.query.get(int(bid))

    def __repr__(self):
        return '<Bookmark %r>' % (self.body)