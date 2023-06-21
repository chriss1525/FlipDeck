#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

DB_NAME = "database.db"


# initialize the app
def create_app():
    app = Flask(__name__, template_folder='../templates',
                static_folder='../static')
    app.config['SECRET_KEY'] = 'secretkey?'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .routes import routes
    from .auth import auth

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Deck, Card

    create_database(app)

    return app


def create_database(app):
    if not path.exists('webapp/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')

