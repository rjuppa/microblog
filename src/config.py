import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    #
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@172.17.0.2/microblog"
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    OAUTH_CREDENTIALS = {
    'facebook': {'id': '470154729788964', 'secret': '010cc08bd4f51e34f3f3e684fbdea8a7'},
    'twitter': {'id': '3RzWQclolxWZIMq5LJqzRZPTl', 'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'},
    'google': {'id': '687414253892-bujl0i5tr8fb18js22dm4sq0r2b2ick0.apps.googleusercontent.com', 'secret': 'OpRHPeuF5-gZfTSbwT24fdzO'}
    }

    # mail server settings
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USERNAME = None
    MAIL_PASSWORD = None

    # administrator list
    ADMINS = ['rjuppa@gmail.com']

    # pagination
    POSTS_PER_PAGE = 50
    MAX_SEARCH_RESULTS = 50


class ProductionConfig(Config):
    DEBUG = False
    if 'DATABASE_URL' in os.environ:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@172.17.0.2/microblog"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')

