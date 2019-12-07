from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request
import album

@route('/')
def server_root():
    with open('index.html', 'r', encoding='UTF-8') as INDEX_FILE:
        OUTPUT_ = INDEX_FILE.read()
    return OUTPUT_

@route('/albums', method='POST')
def add_new_album():
    input_encoding = 'utf8'
    try:
        YEAR_ = int(request.forms.get('year'))
    except:
        YEAR_ = None
    GENRE_ = str(request.forms.get('genre')).strip()
    ARTIST_ = str(request.forms.get('artist')).strip()
    ALBUM_ = str(request.forms.get('album')).strip()
    assert len(ALBUM_) > 0, 'Заполните поле <Название альбома>'
    assert len(ARTIST_) > 0, 'Заполните поле <Артист или группа>'
    assert album.if_not_exist(ARTIST_, ALBUM_), 'Такой альбом группы уже есть в базе'
    DEVNULL_ = album.add_album(YEAR_, ARTIST_, GENRE_, ALBUM_)
    OUTPUT_ = '<P><A HREF="/">Вернуться на Home Page</A></P>'
    OUTPUT_ += 'Альбом <B>' + ARTIST_ + ' -- ' + ALBUM_ +'</B> добавлен в базу.'
    return OUTPUT_

@route('/albums/<artist>')
def albums_count(artist):
    if artist == 'all':
        ALBUMS_LIST = album.show_all()
        ALL_ALBUM_BASE = []
        for ALBUM_ in ALBUMS_LIST:
            ALBUM_STRING = ALBUM_.artist + ' -- ' + ALBUM_.album + ' (' + str(ALBUM_.year) + ') ' + ALBUM_.genre
            ALL_ALBUM_BASE.append(ALBUM_STRING)
        ALBUMS_SUM = len(ALL_ALBUM_BASE)
        OUTPUT_ = '<P><A HREF="/">Вернуться на Home Page</A></P>'
        OUTPUT_ += 'Всего в базе найдено <B>' + str(ALBUMS_SUM) + '</B> альбомов:<BR><OL><LI>'
        OUTPUT_ += '</LI><LI>'.join(ALL_ALBUM_BASE)
        OUTPUT_ += '</LI>'
        return OUTPUT_
    else:
        ALBUMS_LIST = album.find_artist(artist)
        if not ALBUMS_LIST:
            ERRMSG_ = 'Альбомов {} не найдено'.format(artist)
            OUTPUT_ = HTTPError(404, ERRMSG_)
        else:
            ALBUM_NAMES = [album.album for album in ALBUMS_LIST]
            ALBUMS_SUM = len(ALBUM_NAMES)
            OUTPUT_ = '<P><A HREF="/">Вернуться на Home Page</A></P>'
            OUTPUT_ += 'В базе найдено <B>{}</B> альбомов <B>{}</B>:<BR><OL><LI>'.format(ALBUMS_SUM, artist)
            OUTPUT_ += '</LI><LI>'.join(ALBUM_NAMES)
            OUTPUT_ += '</LI>'
        return OUTPUT_

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
