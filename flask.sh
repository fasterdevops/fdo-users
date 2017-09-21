#!/bin/sh
# flask.sh - run flask website define by FLASK_APP

export FLASK_APP='/home/flask/usermanager.py'
flask run --host=0.0.0.0 --port=80
