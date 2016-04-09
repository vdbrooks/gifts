from flask import Flask, request, render_template
from user import User, db

app = Flask(__name__)

@app.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    if request.method == 'POST':
        try:
            new_user = User(request.form['username'], request.form['email'],request.form['password'])
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return 'Username already in use'
        return "Storing new user: {}".format(request.form['email'])

    else:
        return render_template('signup.html', error=error)

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User('admin', 'admin@example.com')
        return "Storing new user: {}".format(request.form['email'])
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

if __name__ == "__main__":
    app.run(debug=True)
