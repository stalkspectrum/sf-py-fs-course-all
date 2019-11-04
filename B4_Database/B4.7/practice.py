import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = 'sqlite:///b4_7.sqlite3'
Base = declarative_base()

class Album(Base):
    __tablename__ = 'album'
    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

'''
engine = sa.create_engine(DB_PATH)
Sessions = sessionmaker(engine)
session = Sessions()

albums = session.query(Album).all()
#print(len(albums))
for album in albums:
    #print(album.year, album.artist, album.genre, album.album)
    print('Группа {} записала альбом {} в жанре {} в {} году'.format(album.artist, album.album, album.genre, album.year))
'''

def parse_connection_string(connection_string):
    ##### dialect+driver://username:password@host:port/database
    ##### dialect | driver | username | password | host | port | database
    con_dict = {
        'dialect': '',
        'driver': '',
        'username': '',
        'password': '',
        'host': '',
        'port': '',
        'database': '',
        'rest': ''
    }
    FIRST_PLUS = connection_string.find('+')
    FIRST_URL = connection_string.find('://')
    if connection_string.find('+') == -1 or connection_string.find('+') > connection_string.find('://'):
        con_dict['dialect'] = connection_string[:connection_string.find('://')]
        connection_string = connection_string.replace((con_dict['dialect'] + '://'), '', 1)
    else:
        con_dict['dialect'] = connection_string[:connection_string.find('+')]
        connection_string = connection_string.replace((con_dict['dialect'] + '+'), '', 1)
        con_dict['driver'] = connection_string[:(connection_string.find('://'))]
        connection_string = connection_string.replace(con_dict['driver'], '', 1).replace('://', '', 1)
    if connection_string[0] == '/':
        con_dict['database'] = connection_string.replace('/', '', 1)
        connection_string = ''
    else:
        con_dict['database'] = connection_string[(connection_string.rfind('/') + 1):]
        connection_string = connection_string.replace(('/' + con_dict['database']), '')
    FIRST_COLON = connection_string.find(':')
    FIRST_AT = connection_string.find('@')
    if FIRST_COLON > -1 and (FIRST_AT > FIRST_COLON or FIRST_AT == -1):
        con_dict['username'] = connection_string[:FIRST_COLON]
        connection_string = connection_string.replace((con_dict['username'] + ':'), '', 1)
    if connection_string.rfind('@') > -1:
        con_dict['password'] = connection_string[:connection_string.rfind('@')]
        connection_string = connection_string.replace((con_dict['password'] + '@'), '', 1)
    FIRST_COLON = connection_string.find(':')
    if FIRST_COLON == -1:
        con_dict['host'] = connection_string
    else:
        con_dict['host'] = connection_string[:FIRST_COLON]
        connection_string = connection_string.replace((con_dict['host'] + ':'), '')
        con_dict['port'] = connection_string

    con_dict['rest'] = connection_string
    return con_dict

if __name__ == '__main__':
    #print(parse_connection_string('sqlite3:///b4_7.sqlite3'))
    print(parse_connection_string('postgresql+psycopg2://admin:as%dr+4@sd:#_-r!f$g@localhost.ru:1443/b4_7'))
    print(parse_connection_string('postgresql+psycopg2://admin:as%dr+4@sd:#_-r!f$g@localhost.ru/b4_7'))
    #print(parse_connection_string('m2sql://admin:as%dr+4@sd:#_-r!f$g/b4_7'))
