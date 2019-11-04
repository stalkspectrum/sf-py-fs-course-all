import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)

def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def valid_email(email):
    return '@' in email and '.' in email.split('@')[1]

def request_data():
    print('---=== Сбор данных о пользователе ===---')
    first_name = input('Имя: ')
    last_name = input('Фамилия: ')
    gender_draft = input('Пол (Male, M, m, М, м или Female, F, f, Ж, ж: ')
    if gender_draft[0] in ['M', 'm', 'М', 'м']:
        gender = 'Male'
    elif gender_draft[0] in ['F', 'f', 'Ж', 'ж']:
        gender = 'Female'
    else:
        gender = gender_draft
    email_draft = input('Адрес электронной почты: ')
    if valid_email(email_draft):
        email = email_draft
    else:
        email = 'nobody@nowhere.never'
    birthdate = input('Дата рождения (YYYY-MM-DD): ')
    height = float(input('Рост в метрах: '))
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user

def main():
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print('Данные пользователя введены в базу.')

if __name__ == '__main__':
    main()
