from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        return "Storing new user: {}".format(request.form['email'])
        self.password = password
        self.password = password
        self.password = password
    else:
        return render_template('login.html', error=error)
        
    return "Hello World!"

