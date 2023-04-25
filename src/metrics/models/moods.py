import metrics.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.moods


def create(email, mood):
    connect().insert_one({'email': str(email), 'mood': int(mood)})


def read(email):
    return connect().find({'email': str(email)})
