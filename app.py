#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Initial app."""


from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Índice del proyecto."""
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9608, debug=True)

# END
