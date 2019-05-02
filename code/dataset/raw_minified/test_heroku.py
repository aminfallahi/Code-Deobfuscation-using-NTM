from flask import Flask
from flask_appconfig import HerokuConfig as B
def A():A=Flask('testapp');B(A);return A
def C(monkeypatch):C='heroku-db-uri';monkeypatch.setenv('HEROKU_POSTGRESQL_ORANGE_URL',C);B=A();assert B.config['SQLALCHEMY_DATABASE_URI']==C