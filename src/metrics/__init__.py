from flask import Flask, request
import secrets, jwt

import metrics.models.users as users_model


app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/metrics/login')
def login():
    if not 'username' in request.json: raise errors.DataError()
    if not 'password' in request.json: raise errors.DataError()

    username = request.json['username']
    password = request.json['password']

    if users_model.read_one(username) == None:
        users_model.create(username)
        key = jwt.encode({'username': username}, app.secret_key, algorithm = 'HS256')

    else:
        user = users_model.read_one(username)
        if helpers.verify_password(user['password'], password):
            key = users_model.new_key(username)

        else: raise errors.AuthError()

    return {'Authorization': key}
