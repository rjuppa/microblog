#!~/venv/py34f/bin/python3.4
from flask import Flask
from migrate.versioning import api
from app import db
import os.path

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
cfg = app.config

db.create_all()
if not os.path.exists(cfg['SQLALCHEMY_MIGRATE_REPO']):
    api.create(cfg['SQLALCHEMY_MIGRATE_REPO'], 'database repository')
    api.version_control(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'])
else:
    api.version_control(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'], api.version(cfg['SQLALCHEMY_MIGRATE_REPO']))