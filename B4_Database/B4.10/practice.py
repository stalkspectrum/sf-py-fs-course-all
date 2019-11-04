import uuid
import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = 'sqlite:///users.sqlite3'
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.String(36), primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    email = sa.Column(sa.Text)

class LastSeenLog(Base):
    __tablename__ = 'log'
    id = sa.Column(sa.String(36), primary_key=True)
    timestamp = sa.Column(sa.DATETIME)

def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def valid_email(email):
    return '@' in email and '.' in email.split('@')[1]

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
    user = User(
        id=user_id,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    return user

def find(name, session):
    query = session.query(User).filter(User.first_name == name)
    users_cnt = query.count()
    user_ids = [user.id for user in query.all()]
    last_seen_query = session.query(LastSeenLog).filter(LastSeenLog.id.in_(user_ids))
    log = {log.id: log.timestamp for log in last_seen_query.all()}
    return (users_cnt, user_ids, log)

def update_timestamp(user_id, session):
    log_entry = session.query(LastSeenLog).filter(LastSeenLog.id == user_id).first()
    if log_entry is None:
        log_entry = LastSeenLog(id=user_id)
    log_entry.timestamp = datetime.datetime.now()
    return log_entry

def print_users_list(cnt, user_ids, last_seen_log):
    if user_ids:
        print('Users found: ', cnt)
        print('User ID --- Last seen date')
        for user_id in user_ids:
            last_seen = last_seen_log[user_id]
            print('{} --- {}'.format(user_id, last_seen))
    else:
        print('There are not any user with such name.')

def main():
    session = connect_db()
    mode = input('Choose mode:\n1 - search user by name\n2 - write new user data\n')
    if mode == '1':
        name = input('User name to find: ')
        users_cnt, user_ids, log = find(name, session)
        print_users_list(users_cnt, user_ids, log)
    elif mode == '2':
        user = request_data()
        session.add(user)
        log_entry = update_timestamp(user.id, session)
        session.add(log_entry)
        session.commit()
        print('Data saved. Thanx!')
    else:
        print('Sorry, wrong mode. =(')

if __name__ == '__main__':
    main()
