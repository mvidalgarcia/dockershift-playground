# This file is part of dockershift-playground.
# Copyright (C) 2017 CERN
#
# dockershift-playground is free software; you can redistribute it
# and/or modify it under the terms of the Revised BSD License.

from __future__ import unicode_literals

import os

from flask import Flask
app = Flask(__name__)
app.config.from_pyfile(os.environ['CONFIG_FILE'], silent=True)


@app.route('/')
def hello_world():
    return 'Hello, {}!'.format(app.config['WHO'])


def main():
    app.run(port=8000)


main()