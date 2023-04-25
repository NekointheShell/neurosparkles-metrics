import secrets
import metrics.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.users


def create(email, password):
    key = secrets.token_hex()
    connect().insert_one({
        'email': str(email),
        'password': str(helpers.hash(password)),
        'key': str(helpers.hash(key))
    })

    return key


def read():
    return connect().find()


def read_one(email):
    return connect().find_one({'email': str(email)})


def read_by_key(key):
    collection = connect()

    for user in collection.find():
        if helpers.verify_password(user['key'], key): return user

    return None


def new_key(email)
    key = secrets.token_hex()
    connect().update_one({'email': str(email)}, {'$set': {'key': str(key)}})

    return key
