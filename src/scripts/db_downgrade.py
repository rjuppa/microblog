#!~/venv/py34f/bin/python3.4
from flask import Flask
from migrate.versioning import api
app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
cfg = app.config
v = api.db_version(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'])
api.downgrade(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'], v - 1)
v = api.db_version(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'])
print('Current database version: ' + str(v))