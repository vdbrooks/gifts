from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash
from app import app
from app import db, models

@app.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    if request.method == 'POST':
        try:
            u = models.User(username=request.form['username'], email=request.form['email'], password=request.form['password'])
            db.session.add(u)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return 'Username already in use: {}'.format(str(e))
        return "Storing new user: {}".format(request.form['email'])

    else:
        return render_template('signup.html', error=error)

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User('admin', 'admin@example.com')
        return "Storing new user2: {}".format(request.form['email'])
    else:
        return render_template('signup.html', error=error)

    return "Hello World!"

@app.route("/limits")
def limits():
    return render_template('template.html', asg_limit=response['MaxNumberOfAutoScalingGroups'],lc_limit=response['MaxNumberOfLaunchConfigurations'])

@app.route('/user/<user>/', methods=['GET', 'POST'])
def user(user=None):
    if request.method == 'GET':
        return render_template('template.html', user=user)

    else:
        return 'Post is not currently supported: {} '.format(user)
