import json
import os
import uuid
DATA_FILE_PATH = 'users.json'
def read():
    if not os.path.exists(DATA_FILE_PATH):
        return []
    with open(DATA_FILE_PATH) as fd:
        users = json.load(fd)
    return users
def save(users):
    with open(DATA_FILE_PATH, 'w') as fd:
        json.dump(users, fd)
def find(users):
    name = input('User name to find: ')
    for user in users:
        if user['first_name'] == name:
            return user['id']
def request_data():
    print('Hi there! I will write your data.')
    first_name = input('Your name: ')
    last_name = input('Your family name: ')
    email_draft = input('Your Email: ')
    if valid_email(email_draft):
        email = email_draft
    else:
        email = 'nobody@nowhere.no'
        print('You wrote wrong mail address!')
    user_id = str(uuid.uuid4())
    user = {
        'id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }
    return user
def valid_email(email):
    return '@' in email and '.' in email.split('@')[1]
def main():
    users_list = read()
    mode = input('Choose mode:\n1 - search user by name\n2 - write new user data\n')
    if mode == '1':
        user_id = find(users_list)
        if user_id:
            print('Found user with UUID = ', user_id)
        else:
            print('There is no such user.')
    elif mode == '2':
        user = request_data()
        users_list.append(user)
        save(users_list)
        print('Data saved. Thanx!')
    else:
        print('Sorry, wrong mode. =(')

if __name__ == '__main__':
    main()
