import os, secrets
import pymongo, argon2, jwt
from flask import request

import metrics.errors as errors


secret_key = secrets.token_hex()


def connect_db():
    client = pymongo.MongoClient(os.environ['MONGO_URL'])
    database = client.metrics

    return client, database


def hash(password):
    hasher = argon2.PasswordHasher()
    return hasher.hash(password)


def verify_password(hash, password):
    hasher = argon2.PasswordHasher()

    if hasher.verify(hash, password): return True
    else: return False


def create_jwt(username):
    return jwt.encode({'username': str(username)}, secret_key, algorithm = 'HS256')


def auth():
    if not 'Authorization' in request.headers: raise errors.AuthError()

    username = jwt.decode(request.headers['Authorization'], secret_key, algorithms = ['HS256'])
    user = users_model.read_one(username)
    if user == None: raise errors.AuthError()

    return user
