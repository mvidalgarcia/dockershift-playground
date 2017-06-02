# This file is part of dockershift-playground.
# Copyright (C) 2017 CERN
#
# dockershift-playground is free software; you can redistribute it
# and/or modify it under the terms of the Revised BSD License.

from __future__ import unicode_literals

from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('hello.cfg', silent=True)


@app.route('/')
def hello_world():
    return 'Hello, {}!'.format(app.config['WHO'])

