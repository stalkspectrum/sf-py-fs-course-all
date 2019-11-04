import json
import os
import uuid
import time
import datetime

USERS_DATA_FILE_PATH = 'users.json'
LOG_DATA_FILE_PATH = 'last_seen_log.json'

class Users:
    def __init__(self):
        self.users = self.read()
    def read(self):
        if not os.path.exists(USERS_DATA_FILE_PATH):
            return []
        with open(USERS_DATA_FILE_PATH) as fd:
            users = json.load(fd)
        return users
    def save(self):
        with open(USERS_DATA_FILE_PATH, 'w') as fd:
            json.dump(self.users, fd)
    def find(self, name):
        for user in self.users:
            if user['first_name'] == name:
                return user['id']
    def add_user(self, user_data):
        self.users.append(user_data)
        self.save()

class LastSeenLog:
    def __init__(self):
        self.log = self.read()
    def read(self):
        if not os.path.exists(LOG_DATA_FILE_PATH):
            return {}
        with open(LOG_DATA_FILE_PATH) as fd:
            log = json.load(fd)
        return log
    def save(self):
        with open(LOG_DATA_FILE_PATH, 'w') as fd:
            json.dump(self.log, fd)
    def update_timestamp(self, user_id):
        current_timestamp = time.time()
        self.log[user_id] = current_timestamp
        self.save()
    def find(self, user_id):
        if user_id in self.log:
            last_seen_time_stamp = self.log[user_id]
            last_seen_date_time = datetime.datetime.fromtimestamp(last_seen_time_stamp)
            last_seen_iso_format = last_seen_date_time.isoformat()
            return last_seen_iso_format
            #return self.log[user_id]

def request_data():
    print('Hi there! I will write your data.')
    first_name = input('Your name: ')
    last_name = input('Your family name: ')
    email_draft = input('Your Email: ')
    if valid_email(email_draft):
        email = email_draft
    else:
        email = 'nobody@nowhere.never'
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
    users = Users()
    last_seen_log = LastSeenLog()
    mode = input('Choose mode:\n1 - search user by name\n2 - write new user data\n')
    if mode == '1':
        name = input('User name to find: ')
        user_id = users.find(name)
        if user_id:
            last_seen = last_seen_log.find(user_id)
            print('Found user with UUID = ', user_id)
            print('User\'s last activity timestamp: ', last_seen)
        else:
            print('There is no such user.')
    elif mode == '2':
        user_data = request_data()
        users.add_user(user_data)
        last_seen_log.update_timestamp(user_data['id'])
        print('Data saved. Thanx!')
    else:
        print('Sorry, wrong mode. =(')

if __name__ == '__main__':
    main()
