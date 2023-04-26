import csv

from flask import (Flask, jsonify, render_template, request, redirect, url_for,
                   flash, get_flashed_messages)

from save_users_to_json import add_user_to_json_file, read_json_data
from data import generate_companies

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'


@app.route('/')
def hello_world():
    return 'Welcome to Flask'


@app.get('/users')
def show_users():
    list_of_users = read_json_data()
    word = request.args.get('word', '')
    filtered_users = filter(lambda elem: word in elem['username'],
                            list_of_users)
    messages = get_flashed_messages(True)
    return render_template(
        'users.html',
        users=filtered_users,
        messages=messages,
    )


@app.post('/users')
def create_new_user():
    email = request.form.get('email', '')
    username = request.form.get('username', '')
    if not username or not email:
        return render_template('user_new.html')
    add_user_to_json_file(username, email)
    flash('User was added successfully', category='success')
    return redirect(url_for('show_users'), code=302)


@app.route('/user/new')
def new_user():
    return render_template('user_new.html')


@app.get('/user/<int:id>')
def user_detail(id):
    data = read_json_data()
    filtered_data = filter(lambda elem: elem['id'] == id, data)
    user = next(filtered_data)
    if user:
        return render_template(
            'user_details.html',
            user=user,
        )
    return 'User with such id is not found', 404
