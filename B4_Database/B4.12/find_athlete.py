import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class Sportsman(Base):
    __tablename__ = 'athelete'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    age = sa.Column(sa.Integer)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.Float)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.Integer)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals = sa.Column(sa.Integer)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)

class User(Base):
    __tablename__ = 'user'
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

def find_user_by_id(USER_NUM, session):
    QUERY = session.query(User).filter(User.id == USER_NUM)
    USER_BIRTHDATE = [USER.birthdate for USER in QUERY]
    USER_HEIGHT = [USER.height for USER in QUERY]
    return USER_BIRTHDATE, USER_HEIGHT

def find_sportsman_by_bdate(BDATE, session):
    B_DELTA_MIN = 10000000      ##### Начальное значение можно задать "почти бесконечным" для данной задачи
    digidate = lambda DD: int(DD.split('-')[0]) * 365 + int(DD.split('-')[1]) * 30 + int(DD.split('-')[2])
    SPORTSMEN = session.query(Sportsman).all()
    SPORTSMEN_B_DICT = {S_MEN.name: S_MEN.birthdate for S_MEN in SPORTSMEN}
    for S_NAME, S_BDATE in SPORTSMEN_B_DICT.items():
        if S_BDATE is None:
            continue
        B_DELTA = abs(digidate(S_BDATE) - digidate(BDATE))
        if B_DELTA < B_DELTA_MIN:
            B_DELTA_MIN = B_DELTA
            B_NAME = S_NAME
            B_DATE = S_BDATE
    return B_NAME, B_DATE

def find_sportsman_by_height(TALL, session):
    H_DELTA_MIN = 5.0     ##### Начальное значение можно задать "почти бесконечным" для данной задачи
    SPORTSMEN = session.query(Sportsman).all()
    SPORTSMEN_H_DICT = {S_MEN.name: S_MEN.height for S_MEN in SPORTSMEN}
    for S_NAME, S_HEIGHT in SPORTSMEN_H_DICT.items():
        if S_HEIGHT is None:
            continue
        H_DELTA = abs(S_HEIGHT - TALL)
        if H_DELTA < H_DELTA_MIN:
            H_DELTA_MIN = H_DELTA
            H_NAME = S_NAME
            H_HEIGHT = S_HEIGHT
    return H_NAME, H_HEIGHT

def main():
    session = connect_db()
    USER_ID = int(input('Введите номер пользователя (целое число): '))
    USER_B, USER_H = find_user_by_id(USER_ID, session)
    if USER_B == [] or USER_H == []:
        print('Нет пользователя с таким номером.')
    else:
        SH_NAME, SH_HEIGHT = find_sportsman_by_height(USER_H[0], session)
        print('Ближайший спортсмен по росту - {} ({}м)'.format(SH_NAME, SH_HEIGHT))
        SB_NAME, SB_DATE = find_sportsman_by_bdate(USER_B[0], session)
        print('Ближайший спортсмен по возрасту - {} (род. {})'.format(SB_NAME, SB_DATE))
    session.commit()

if __name__ == '__main__':
    main()
