from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Flask it is very easy hello'


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users_post():
    return 'POST /users', 302


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'
