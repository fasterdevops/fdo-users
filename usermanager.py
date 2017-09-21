#!/usr/bin/env python
'''
User Manager
'''

from flask import *


app = Flask(__name__)
file = 'index.html'

@app.route('/')
def hello_world():
    return render_template(file)
