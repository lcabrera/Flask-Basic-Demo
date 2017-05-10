# -*- coding: utf-8 -*-

"""Configuración del proyecto."""

# import os
import tempfile

db_file = tempfile.NamedTemporaryFile()


class Config(object):
    """Config class.

    Una manera de obtener una 'SECRET_KEY' de calidad es la siguiente:

        python -c "import os; print repr(os.urandom(24));"

    Se podría aplicar, incluso, de forma dinámica.
    """

    # Genérico
    # ~~~~~~~~
    SECRET_KEY = 'secret key'
    GOOGLE_ANALYTICS = ''
    # APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    # PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    # Flask settings
    # ~~~~~~~~~~~~~~
    APP_NAME = 'Web PICSL'
    APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + ' system error'
    CSRF_ENABLED = True

    # Flask_bcrypt
    # ~~~~~~~~~~~~
    BCRYPT_LOG_ROUNDS = 13

    # Flask_assets
    # ~~~~~~~~~~~~
    ASSETS_DEBUG = False

    # Flask_debugtoolbar
    # ~~~~~~~~~~~~~~~~~~
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Flask_cache
    # ~~~~~~~~~~~
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    CACHE_NO_NULL_WARNING = True

    # Flask_mail
    # ~~~~~~~~~~
    MAIL_USERNAME = 'email@example.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '"Sender" <noreply@example.com>'
    MAIL_SERVER = 'smtp.mail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False

    # Flask-SQLAlchemy
    # ~~~~~~~~~~~~~~~~
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-User
    # ~~~~~~~~~~
    USER_APP_NAME = APP_NAME
    USER_ENABLE_CHANGE_PASSWORD = True  # Allow users to change their password
    USER_ENABLE_CHANGE_USERNAME = False  # Allow users to change their username
    USER_ENABLE_CONFIRM_EMAIL = True  # Force users to confirm their email
    USER_ENABLE_FORGOT_PASSWORD = True  # Allow users to reset their passwords
    USER_ENABLE_EMAIL = True  # Register with Email
    USER_ENABLE_REGISTRATION = True  # Allow new users to register
    USER_ENABLE_RETYPE_PASSWORD = True  # Prompt for `retype password` in:
    USER_ENABLE_USERNAME = False  # Register and Login with username
    USER_AFTER_LOGIN_ENDPOINT = 'user_page'
    USER_AFTER_LOGOUT_ENDPOINT = 'home_page'


class ProdConfig(Config):
    """Producción."""

    ENV = 'prod'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database' + ENV + '.db'
    SQLALCHEMY_MIGRATE_REPO = 'db_repository_' + ENV
    CACHE_TYPE = 'simple'


class DevConfig(Config):
    """Desarrollo."""

    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLED = True  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database' + ENV + '.db'
    SQLALCHEMY_MIGRATE_REPO = 'db_repository_' + ENV

    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True


class TestConfig(Config):
    """Test..."""

    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    SQLALCHEMY_MIGRATE_REPO = 'db_repository_' + ENV
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
