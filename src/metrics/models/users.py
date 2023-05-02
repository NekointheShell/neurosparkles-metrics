import metrics.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.users


def create(username, password):
    connect().insert_one({
        'username': str(username),
        'password': str(helpers.hash(password))
    })


def read():
    return connect().find()


def read_one(username):
    return connect().find_one({'username': str(username)})
