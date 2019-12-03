import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = 'sqlite:///albums.sqlite3'
Base = declarative_base()

class Album(Base):
    __tablename__ = 'album'
    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

def connect_db():
    DB_CONNECTOR = sa.create_engine(DB_PATH)
    Base.metadata.create_all(DB_CONNECTOR)
    FACTORY_SESSIONS = sessionmaker(DB_CONNECTOR)
    return FACTORY_SESSIONS()

def show_all():
    SESSION_S = connect_db()
    ALBUMS_ALL = SESSION_S.query(Album).all()
    return ALBUMS_ALL

def find_artist(ARTIST_R):
    SESSION_F = connect_db()
    albums = SESSION_F.query(Album).filter(Album.artist == ARTIST_R).all()
    return albums

''' НЕПРАВИЛЬНО
def if_already_exist(ARTIST_, ALBUM_):
    SESSION_I = connect_db()
    ID_ = select([Album.id]).where(Album.album == ALBUM_)
    if select([Album.artist]).where(Album.id == ID_) == ARTIST_:
        return True
    else:
        return False
'''

def add_album(YEAR_F, ARTIST_F, GENRE_F, ALBUM_F):
    new_album_data = Album(year=YEAR_F, artist=ARTIST_F, genre=GENRE_F, album=ALBUM_F)
    SESSION_W = connect_db()
    SESSION_W.add(new_album_data)
    SESSION_W.commit()
    return 'NEW Album added to DATABASE!'
