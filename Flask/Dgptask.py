#!/usr/bin/env python
# coding: latin-1
import flask
# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at ’/’
    """
    return flask.render_template('index.html')

@APP.route('/welcome/<name>/')
def welcome(name):
    return flask.render_template('welcome.html',name=name)  # render a template

if __name__ == '__main__':
    APP.run(debug=False)
