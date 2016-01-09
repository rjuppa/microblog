import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from .momentjs import momentjs, use_html
from flask.ext.mail import Mail

from config import basedir

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
app.jinja_env.globals['momentjs'] = momentjs
app.jinja_env.globals['use_html'] = use_html
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

mail = Mail(app)

from app import views, models




# logging to email
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if app.config.MAIL_USERNAME or app.config.MAIL_PASSWORD:
        credentials = (app.config.MAIL_USERNAME, app.config.MAIL_PASSWORD)
    mail_handler = SMTPHandler((app.config.MAIL_SERVER, app.config.MAIL_PORT), 'no-reply@' + app.config.MAIL_SERVER, app.config.ADMINS, 'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

# logging to console
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')