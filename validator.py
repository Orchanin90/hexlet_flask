from save_users_to_json import read_json_data


def validate(username, email):
    errors = {}
    if username is None:
        errors['username'] = 'Can not be blank'
    if email is None:
        errors['email'] = 'Can not be blank'
    if len(username) < 2:
        errors['username'] = 'Can not be less than 2 symbols'
    if len(email) < 4:
        errors['email'] = 'Can not be less than 4 symbols'
    return errors


def validator_for_updating_user(email):
    errors = {}
    if email is None:
        errors['email'] = 'Can not be blank'
    elif len(email) < 4:
        errors['email'] = 'Can not be less than 4 symbols'
    return errors


def is_email_in_data(email):
    errors = {}
    data = read_json_data()
    for elem in data:
        if elem['email'] == email:
            return errors
    errors['email'] = 'There is no such email'
    return errors


