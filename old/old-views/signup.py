from flask import Flask, request, render_template
from user import User, db

app = Flask(__name__)

@app.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    if request.method == 'POST':
        new_user = User(request.form['username'], request.form['email'],request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return "Storing new user: {}".format(request.form['email'])
    else:
        return render_template('signup.html', error=error)
        
    #return "Hello World!"

