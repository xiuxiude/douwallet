from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import douwallet.views.home


db = SQLAlchemy()


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

    # registers blueprints
    app.register_blueprint(douwallet.views.home.bp)

    return app
