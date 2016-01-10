#!~/venv/py34f/bin/python3.4
from migrate.versioning import api
from flask import Flask
app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
cfg = app.config

api.upgrade(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'])
v = api.db_version(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'])
print('Current database version: ' + str(v))
