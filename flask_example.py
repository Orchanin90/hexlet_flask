import csv
import json

from flask import (Flask, jsonify, render_template, request, redirect, url_for,
                   flash, get_flashed_messages, make_response, session)

from save_users_to_json import (add_user_to_json_file, read_json_data,
                                update_user_email, remove_user_from_data)
from data import generate_companies
from validator import (validate, validator_for_updating_user, is_email_in_data)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'


@app.route('/')
def hello_world():
    return '<a href="/users">Welcome to Flask</a>'


@app.get('/users')
def show_users():
    print(session)
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
    email = request.form.get('email', None)
    username = request.form.get('username', None)
    errors = validate(username, email)
    if errors:
        return render_template(
            'user_new.html',
            errors=errors,
            email=email,
            username=username
        ), 422
    add_user_to_json_file(username, email)
    flash('User was added successfully', category='success')
    return redirect(url_for('show_users'), code=302)


@app.route('/user/new')
def new_user():
    errors = {}
    username = ''
    email = ''
    return render_template(
        'user_new.html',
        errors=errors,
        username=username,
        email=email,
    )


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


@app.route('/users/<int:id>/update', methods=['POST', 'GET'])
def update_user(id):
    data = read_json_data()
    filtered_data = filter(lambda elem: elem['id'] == id, data)
    user = next(filtered_data)
    errors = {}

    if request.method == 'GET':
        return render_template(
            'user_edit.html',
            user=user,
            errors=errors,
        )

    if request.method == 'POST':
        email = request.form.get('email')
        errors = validator_for_updating_user(email)
        if errors:
            return render_template(
                'user_edit.html',
                errors=errors,
                user=user,
            )
        update_user_email(user, email)
        flash('User was updated successfully', 'success')
        return redirect(url_for('show_users'))


@app.route('/user/<int:id>/delete', methods=['POST'])
def delete_user(id):
    remove_user_from_data(id)
    flash('User was deleted successfully', 'success')
    return redirect(url_for('show_users'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    errors = {}
    email = request.form.get('email', '')

    if request.method == 'POST':
        errors = is_email_in_data(email)
        if errors:
            return render_template(
                'login.html',
                email=email,
                errors=errors
            ), 302
        session.setdefault('is_user_logged', []).append(email)
        flash('You are logged', 'success')
        return redirect(url_for('show_users'))

    if request.method == 'GET':
        return render_template(
            'login.html',
            email=email,
            errors=errors
        )
