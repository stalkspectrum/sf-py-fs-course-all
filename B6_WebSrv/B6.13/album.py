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
    SESSIONS_FACTORY = sessionmaker(DB_CONNECTOR)
    return SESSIONS_FACTORY()

def show_all():
    SESSION_ = connect_db()
    ALL_ALBUMS = SESSION_.query(Album).all()
    return ALL_ALBUMS

def find_artist(ARTIST_):
    SESSION_ = connect_db()
    ALBUMS_ = SESSION_.query(Album).filter(Album.artist == ARTIST_).all()
    return ALBUMS_

def if_not_exist(ARTIST_, ALBUM_):
    SESSION_ = connect_db()
    ID_ = SESSION_.query(Album).filter(Album.artist == ARTIST_, Album.album == ALBUM_).first()
    if ID_ is not None:
        return False
    else:
        return True

def add_album(YEAR_, ARTIST_, GENRE_, ALBUM_):
    new_album_data = Album(year=YEAR_, artist=ARTIST_, genre=GENRE_, album=ALBUM_)
    SESSION_ = connect_db()
    SESSION_.add(new_album_data)
    SESSION_.commit()
    return 'NEW Album added to DATABASE.'
