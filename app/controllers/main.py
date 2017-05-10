#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Controlador principal.

Aquí van todas las rutas y demás.
"""


from app import app


@app.route('/')
def index():
    """Índice del proyecto."""
    return '<h1>Hello World!</h1>'

# END
