from flask import Flask, request, render_template
import boto3

app = Flask(__name__)
asclient = boto3.client('autoscaling')

@app.route("/")
def lo():
    return "Hello World!"

@app.route("/limits")
def limits():
    response = asclient.describe_account_limits()
    return render_template('template.html', asg_limit=response['MaxNumberOfAutoScalingGroups'],lc_limit=response['MaxNumberOfLaunchConfigurations']) 

@app.route('/user/<user>/', methods=['GET', 'POST'])
def user(user=None):
    if request.method == 'GET':
        return render_template('template.html', user=user)
        
    else:
        return 'Post is not currently supported: {} '.format(user)

if __name__ == "__main__":
    app.run(debug=True)
