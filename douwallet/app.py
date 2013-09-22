#!/usr/bin/env python
# encoding: utf-8

from flask import Flask

from models import db
from admin import admin
from auth import login_manager

import views.home
import views.auth


def create_app():
    """Creates an app instance.

    There are only one instance while serving as web server, but multiple
    instances while running tests.
    """
    app = Flask(__name__)

    # loads configuration
    app.config.from_pyfile("app.cfg")
    app.config.from_pyfile("app-dev.cfg", silent=True)
    app.config.from_envvar("DOUWALLET_CONFIG", silent=True)

    # initializes extensions
    db.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)

    # registers blueprints
    app.register_blueprint(views.home.bp)
    app.register_blueprint(views.auth.bp)

    return app
