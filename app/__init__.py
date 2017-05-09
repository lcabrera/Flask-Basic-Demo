# -*- coding: utf-8 -*-

# """FBD
# """


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

app = Flask(__name__)
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

# END
