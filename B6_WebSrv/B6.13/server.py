from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request
import album

@route('/')
def server_root():
    with open('index.html', 'r', encoding='UTF-8') as INDEX_FILE:
        INDEX_HTML = INDEX_FILE.read()
    return INDEX_HTML

@route('/albums', method='POST')
def add_new_album():
    YEAR_N = request.forms.get('year')
    ARTIST_N = request.forms.get('artist')
    GENRE_N = request.forms.get('genre')
    ALBUM_N = request.forms.get('album')
    RES_N = album.add_album(YEAR_N, ARTIST_N, GENRE_N, ALBUM_N)
    RES_D = '<P><A HREF="/">Вернуться на Home Page</A></P>'
    RES_D += 'Альбом <B>' + ARTIST_N + ' -- ' + ALBUM_N +'</B> добавлен в базу.'
    return RES_D

@route('/albums/<artist>')
def albums_count(artist):
    if artist == 'all':
        ALBUM_LIST = album.show_all()
        ALL_ALBUM_BASE = []
        for ALBUM_S in ALBUM_LIST:
            ALBUM_STRING = ALBUM_S.artist + ' -- ' + ALBUM_S.album
            ALL_ALBUM_BASE.append(ALBUM_STRING)
        ALBUM_SUM = len(ALL_ALBUM_BASE)
        RES_A = '<P><A HREF="/">Вернуться на Home Page</A></P>'
        RES_A += 'Всего в базе найдено <B>' + str(ALBUM_SUM) + '</B> альбомов:<BR><OL><LI>'
        RES_A += '</LI><LI>'.join(ALL_ALBUM_BASE)
        RES_A += '</LI>'
        return RES_A
    else:
        ALBUM_LIST = album.find_artist(artist)
        if not ALBUM_LIST:
            MSG_B = 'Альбомов {} не найдено'.format(artist)
            RES_B = HTTPError(404, MSG_B)
        else:
            ALBUM_NAMES = [album.album for album in ALBUM_LIST]
            ALBUM_SUM = len(ALBUM_NAMES)
            RES_B = '<P><A HREF="/">Вернуться на Home Page</A></P>'
            RES_B += 'В базе найдено <B>{}</B> альбомов <B>{}</B>:<BR><OL><LI>'.format(ALBUM_SUM, artist)
            RES_B += '</LI><LI>'.join(ALBUM_NAMES)
            RES_B += '</LI>'
        return RES_B

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
