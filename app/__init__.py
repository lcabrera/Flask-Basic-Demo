# -*- coding: utf-8 -*-

"""Punto de entrada de la aplicación."""

from flask import Flask


# from flask.ext.sqlalchemy import SQLAlchemy  # Setup the database.
# from flask.ext.mail import Mail  # Setup the mail server
# from flask_debugtoolbar import DebugToolbarExtension  # Setup debug toolbar
# from flask.ext.bcrypt import Bcrypt  # Setup the password crypting
# from flask.ext.login import LoginManager  # Setup the user login process

# from app.logger_setup import logger  # Setup the logger
# from app.views import main, user, error  # Import the views
# from app.models import User
# from app import admin


__author__ = 'Luis Cabrera Sauco'
__email__ = 'icorrecam@gmail.com'

# app = Flask(__name__)
# app.config.from_object('app.config')  # Setup the app with the config.py file

# db = SQLAlchemy(app)

# mail = Mail(app)

# # DebugToolBar
# app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
# app.config['DEBUG_TB_PROFILER_ENABLED'] = True
# toolbar = DebugToolbarExtension(app)

# # Setup the password crypting
# bcrypt = Bcrypt(app)

# # Import the views
# app.register_blueprint(user.userbp)

# # Setup the user login process
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'userbp.signin'


# @login_manager.user_loader
# def load_user(email):
#     """Carga de usuarios."""
#     return User.query.filter(User.email == email).first()


def create_app(object_name):
    """Create the app.

    This is a flask application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. webpic.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """
    app = Flask(__name__)

    app.config.from_object(object_name)

    # Initialize Flask extensions

    # Initialize Flask-Mail
    # mail = Mail(app)
    # Mail(app)
    # mail(app)

    # initialize the cache
    # cache.init_app(app)

    # initialize the debug tool bar
    # debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    # db.init_app(app)

    # login_manager.init_app(app)

    # Import and register the different asset bundles
    # assets_env.init_app(app)

    # assets_loader = PythonAssetsLoader(assets)

    # for name, bundle in assets_loader.load_bundles().items():
    #     assets_env.register(name, bundle)

    # register our blueprints
    # app.register_blueprint(main)

    return app

# END
