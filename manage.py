#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Gestión centralizada del proyecto."""

import os

from flask_script import Manager, Server, Shell
from flask_script.commands import Clean, ShowUrls
# from app import db
# from app import models
from termcolor import colored

# from app import app
from app import create_app

# from flask_script import prompt_bool

# TODO

# Ver si es conveniente
# if os.environ.get("NOMBREDELAAPLICACION_ENV") == 'prod':
#    app = create_app(ProdConfig)
# else:
#    app = create_app(DevConfig)

# FIXME

# Otra forma de crear las variables de ambiente:
# default to dev config because no one should use this in
# production anyway
ENV = os.environ.get('APP_ENV', 'dev')
FLASK_APPENV = os.environ.get('FLASK_APP', 'app')
HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')


HOST = '0.0.0.0'
PORT = 9608


app = create_app('app.settings.%sConfig' % ENV.capitalize())

manager = Manager(app)


def make_shell_context():
    """Return context dict.

    Return context for a shell session so you can access app, db, and the
    User model by default.
    """
    # return {'app': app, 'db': db, 'User': User}
    return dict(app=app)


# @manager.command
# def initdb():
#    ''' Create the SQL database. '''
#    db.create_all()
#    print(colored('The SQL database has been created', 'green'))


# @manager.command
# def dropdb():
#    ''' Delete the SQL database. '''
#    if prompt_bool('Are you sure you want to lose all your SQL data?'):
#        db.drop_all()
#        print(colored('The SQL database has been deleted', 'green'))


@manager.command
def hello():
    """Imprime 'hello' por pantalla."""
    print('hello')


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code


manager.add_command('runserver', Server(host=HOST, port=PORT))
manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)
manager.add_command('urls', ShowUrls())
manager.add_command('clean', Clean())


if __name__ == '__main__':
    '''Inicio de la aplicación.'''
    if ENV == 'dev':
        print(colored('\nArrancando...\n', 'green'))
        print(colored('\n%s: estamos en desarrollo.\n', 'green',
              attrs=['reverse', 'bold']) % ENV)
    else:
        print(colored('\nArrancando...\n', 'red'))
        print(colored('\n%s: Estamos en producción.\n', 'red',
              attrs=['reverse', 'bold']) % ENV)

    manager.run()

# END
