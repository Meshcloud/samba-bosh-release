from flask import Flask
from flask import request
from flask import jsonify
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
    exit_code = os.system('sudo get_credentials.sh '+ username + " " + password["password"])
    returnValue = {}
    if exit_code < 256:
        returnValue["password"] = password["password"]
        returnValue["username"] = username
        return jsonify(returnValue)
    else:
        returnValue["failure"] = "failure"
        return jsonify(returnValue)

@app.route("/user/<username>", methods = ["DELETE"])
def delete_credentials(username):
    exit_code = os.system('sudo delete_credentials.sh ' + username)
    returnValue = {}
    if exit_code < 256:
        returnValue["success"] = "success"
        return jsonify(returnValue)
    else:
        returnValue["failure"] = "failure"
        return jsonify(returnValue)
    
if __name__ == '__main__':
    app.config['BASIC_AUTH_FORCE'] = True
    app.run(host = '0.0.0.0',port=5000) 