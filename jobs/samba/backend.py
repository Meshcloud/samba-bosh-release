from flask import Flask
from flask import request
from flask_basicauth import BasicAuth 
import json
import sys
import os

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = '<%= p("rest.user")%>' 
app.config['BASIC_AUTH_PASSWORD'] = '<%= p("rest.password")%>'
basic_auth = BasicAuth(app)

@app.route("/user/<username>", methods = ["POST"])
def create_credentials(username):
    password = request.get_json(force=True)
    exit_code = os.system('echo '+ username + " " + password["password"])
    returnValue = {}
    if exit_code < 256:
        returnValue["password"] = password["password"]
        returnValue["username"] = username
        return returnValue
    else:
        returnValue["failure"] = "failure"
        return returnValue

@app.route("/user/<username>", methods = ["DELETE"])
def delete_credentials(username):
    exit_code = os.system('delete_credentials.sh ' + username)
    if exit_code < 256:
        return "Success"
    else:
        return "Failure"
    
if __name__ == '__main__':
    app.config['BASIC_AUTH_FORCE'] = True
    app.run(debug=True) 