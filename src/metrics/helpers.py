import os
import pymongo, validators, argon2
from flask import request


def connect_db():
    client = pymongo.MongoClient(os.environ['MONGO_URL'])
    database = client.metrics

    return client, database


def validate_email(email):
    try: validators.email(email)
    except validators.ValidationFailure:
        return False

    return True


def hash(password):
    hasher = argon2.PasswordHasher()
    return hasher.hash(password)


def verify_password(hash, password)
    hasher = argon2.PasswordHasher()

    if hasher.verify(hash, password): return True
    else: return False


def auth()
    if not 'authorization' in request.headers: raise errors.AuthError()

    user = users_model.read_by_key(request.headers['authorization'])
    if user == None: raise errors.AuthError()

    return user
