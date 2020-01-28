import sqlalchemy as sa
from app.db import vote_results

if __name__ == '__main__':
    engine = sa.create_engine('sqlite:///my_db.sqlite')
    with engine.begin() as connection:
        select = vote_results.select()
        results = connection.execute(select)
        for id, name, votes in results.fetchall():
            print(id, name, votes)
