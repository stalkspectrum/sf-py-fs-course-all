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

def valid_email(E_MAIL):
    return '@' in E_MAIL and '.' in E_MAIL.split('@')[1]

def request_data():
    print('---=== Сбор данных о пользователе ===---')
    FIRST_NAME = input('Имя: ')
    LAST_NAME = input('Фамилия: ')
    GENDER_DRAFT = input('Пол (Male, M, m, М, м или Female, F, f, Ж, ж: ')
    if GENDER_DRAFT[0] in ['M', 'm', 'М', 'м']:
        GENDER = 'Male'
    elif GENDER_DRAFT[0] in ['F', 'f', 'Ж', 'ж']:
        GENDER = 'Female'
    else:
        GENDER = GENDER_DRAFT
    EMAIL_DRAFT = input('Адрес электронной почты: ')
    if valid_email(EMAIL_DRAFT):
        EMAIL = EMAIL_DRAFT
    else:
        EMAIL = 'nobody@nowhere.never'
    BIRTHDATE = input('Дата рождения (YYYY-MM-DD): ')
    HEIGHT = float(input('Рост в метрах: '))
    USER = User(
        first_name=FIRST_NAME,
        last_name=LAST_NAME,
        gender=GENDER,
        email=EMAIL,
        birthdate=BIRTHDATE,
        height=HEIGHT
    )
    return USER

def main():
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print('Данные пользователя введены в базу.')

if __name__ == '__main__':
    main()
