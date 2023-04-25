from flask import Flask, request


app = Flask(__name__)


@app.route('/metrics/api/login')
def login():
    if not 'email' in request.json: raise errors.DataError()
    if not 'password' in request.json: raise errors.DataError()
    if not helpers.validate_email(request.json['email']): raise errors.DataError()

    email = request.json['email']
    password = request.json['password']

    if users_model.read_one(email) == None: key = users_model.create(email)
    else:
        user = users_model.read_one(email)
        if helpers.verify_password(user['password'], password):
            key = users_model.new_key(email)

        else: raise errors.AuthError()

    return {'apikey': key}


@app.route('/metrics/api/moods', methods = ['GET', 'POST'])
def moods():
    user = helpers.auth()

    if request.method == 'GET':
        ret = []

        moods = moods_model.read(user['email'])
        for mood in moods:
            ret.append({'time': mood['time'], 'mood': mood['mood']})

        return ret

    elif request.method == 'POST':
        if not 'mood' in request.json: raise errors.DataError()
        moods_model.create(user['email'], request.json['mood'])
        return {}


@app.route('/metrics/api/sleep', methods = ['GET', 'POST'])
@app.route('/metrics/api/exercise', methods = ['GET', 'POST'])
@app.route('/metrics/api/food', methods = ['GET', 'POST'])
@app.route('/metrics/api/blood_pressure', methods = ['GET', 'POST'])
@app.route('/metrics/api/spo2', methods = ['GET', 'POST'])
@app.route('/metrics/api/bpm', methods = ['GET', 'POST'])
