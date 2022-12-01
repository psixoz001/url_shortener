from flask import Flask, request, redirect, jsonify, make_response
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required
import uuid, hashlib, random
from werkzeug.security import generate_password_hash, check_password_hash
from database.CreateDB import createDB
from functions.fn_db import  *

app = Flask(__name__)
app.config['SECRET_KEY'] = '%&$*%&$%$*%&$%*$%$'
jwt = JWTManager(app)

@app.route('/register', methods = ["post"])
def registration():
    if request.method == 'POST':
        email = str(request.json.get('email', None))
        password = str(request.json.get('password', None))
        return make_response(database.registration(email, password))

@app.route('/auth', methods = ["post"])
def authorization():
    if request.method == 'POST':
        email = str(request.json.get('email', None))
        password = str(request.json.get('password', None))
        return make_response(database.auth(email, password))





if __name__ == '__main__':
    app.run()

createDB()