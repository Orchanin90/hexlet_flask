import json

json_file = 'users.json'


def read_json_data():
    try:
        with open(json_file, 'r') as f:
            json_data = json.load(f)
            return json_data
    except FileNotFoundError:
        pass


def write_json_data(data):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


def add_user_to_json_file(username, email):
    data = read_json_data()
    last_dict_from_data = data[-1]
    user_id = last_dict_from_data['id'] + 1
    data.append({'username': username, 'email': email, 'id': user_id})
    write_json_data(data)


def write_json(data):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


def update_user_email(user, email):
    data = read_json_data()
    for index, elem in enumerate(data):
        if elem['username'] == user['username']:
            data[index]['email'] = email
    write_json_data(data)


def remove_user_from_data(id):
    data = read_json_data()
    for index, elem in enumerate(data):
        if elem['id'] == id:
            del data[index]
    write_json_data(data)


if __name__ == '__main__':
    # write_json([{'username': 'username', 'email': 'email', 'id': 1}])
    # add_user_to_data('vadim', 'vadim@email')
    # write_json_data('vadim', 'vadim@email')
    print(read_json_data())
    print(type(read_json_data()))
