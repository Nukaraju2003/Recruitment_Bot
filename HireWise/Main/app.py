import json
import os
import time
import flask
import pandas as pd


app = flask.Flask(__name__)
@app.route('/', methods=['GET'])
def homepage():
    return flask.render_template('homepage.html')

@app.route('/darwin/1', methods=['GET'])
def darwin():
    return flask.render_template('chatbot.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return flask.render_template('admin_login.html')
    if flask.request.method == 'GET':
        return flask.render_template('admin_login.html')

    email = flask.request.form['email']
    if email in list(users.keys()):
        if flask.request.form['password'] == users[email]['password']:
            user = User()
            user.id = email
            flask_login.login_user(user)
            return flask.redirect(flask.url_for('billboard'))
    return flask.redirect(flask.url_for('admin'))

@app.route('/admin/billboard')
def billboard():
    return flask.render_template('job_billboard.html')

app.run()