#!~/venv/py34f/bin/python3.4
import imp
from migrate.versioning import api
from app import db
from flask import Flask
app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
cfg = app.config

v = api.db_version(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'])
migration = cfg['SQLALCHEMY_MIGRATE_REPO'] + ('/versions/%03d_migration.py' % (v+1))
tmp_module = imp.new_module('old_model')
old_model = api.create_model(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'])
exec(old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'], tmp_module.meta, db.metadata)
open(migration, "wt").write(script)
api.upgrade(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'])
v = api.db_version(cfg['SQLALCHEMY_DATABASE_URI'], cfg['SQLALCHEMY_MIGRATE_REPO'])
print('New migration saved as ' + migration)
print('Current database version: ' + str(v))
