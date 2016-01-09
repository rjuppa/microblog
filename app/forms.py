from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
from app.models import User


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])


class EditProfileForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True


class ContactForm(Form):
    mail_from = StringField('from', validators=[DataRequired('Please enter your email address.'),
                                                Email('This field requires a valid email address')])
    message = TextAreaField('message', validators=[DataRequired('Please enter message.'),
                                                   Length(min=0, max=800)])


class BookmarksEditForm(Form):
    name = StringField('name', validators=[DataRequired('Please enter bookmark name.')])
    url = StringField('url', validators=[DataRequired('Please enter bookmark url.')])
    tags = StringField('tags')


class PostsEditForm(Form):
    title = StringField('title', validators=[DataRequired('Please enter title.')])
    body = TextAreaField('body', validators=[DataRequired('Please enter body.')])
    delete = BooleanField('delete')
    tags = StringField('tags')