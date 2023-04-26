import json

json_file = 'users.json'


def read_json_data():
    try:
        with open(json_file, 'r') as f:
            json_data = json.load(f)
            return json_data
    except FileNotFoundError:
        return 'File does not exist'


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


if __name__ == '__main__':
    # write_json([{'username': 'username', 'email': 'email', 'id': 1}])
    # add_user_to_data('vadim', 'vadim@email')
    # write_json_data('vadim', 'vadim@email')
    print(read_json_data())
    print(type(read_json_data()))
