#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Gestión centralizada del proyecto."""

from flask_script import Manager, Server, Shell
# from flask_script import prompt_bool

from app import app
# from app import db
# from app import models
from termcolor import colored


# TODO: Ver si es conveniente
# if os.environ.get("NOMBREDELAAPLICACION_ENV") == 'prod':
#    app = create_app(ProdConfig)
# else:
#    app = create_app(DevConfig)

# FIXME: Otra forma de crear las variables de ambiente:
# default to dev config because no one should use this in
# production anyway
# ENV = os.environ.get('PICSLWEB_ENV', 'dev')
# HERE = os.path.abspath(os.path.dirname(__file__))
# TEST_PATH = os.path.join(HERE, 'tests')
# ## app = create_app('picslweb.settings.%sConfig' % ENV.capitalize())


manager = Manager(app)


def make_shell_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
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


manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)
# manager.add_command("urls", ShowUrls())
# manager.add_command("clean", Clean())


if __name__ == '__main__':
    print(colored('Arrancando...\n', 'yellow'))
    manager.run()

# END
