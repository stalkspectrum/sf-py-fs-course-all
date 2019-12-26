'''!!!!!!!!!! USAGE: !!!!!!!!!!
Вывод всех колонок с числом и списком карточек в каждой колонке:
    python trello.py
Создать новую колонку(лист) List_Name на доске:
    python trello.py newlist "List_Name"
Создать карточку Card_Name в колонке(листе) List_Name:
    python trello.py newcard "Card_Name" "List_Name"
Переместить карточку Card_Name в колонку(лист) List_Name:
    python trello.py movecard "Card_Name" "List_Name"
'''

import sys
import requests

USAGE_STR = '\n!!!!!!!!!! USAGE: !!!!!!!!!!\n\
Вывод всех колонок с числом и списком карточек в каждой колонке:\n\
\tpython trello.py\n\n\
Создать новую колонку(лист) List_Name на доске:\n\
\tpython trello.py newlist \"List_Name\"\n\n\
Создать карточку Card_Name в колонке(листе) List_Name:\n\
\tpython trello.py newcard \"Card_Name\" \"List_Name\"\n\n\
Переместить карточку Card_Name в колонку(лист) List_Name:\n\
\tpython trello.py movecard \"Card_Name\" \"List_Name\"\n\
============================\n'

BASE_URL = 'https://api.trello.com/1/{}'

#####!!!!! Вписать свой Board_ID !!!!!#####
BOARD_ID = 'Xv****b8'

#####!!!!! Вписать свои API_key и API_token !!!!!#####
AUTH_PARAMS = {
    'key': '48d9****c42b****4db9****6bc4****',
    'token': 'a03c****a88d****fb5a****8c8b****28a9****f750****bf47****28da****',
}


def find_equals(NEW_LINE, OLD_LINE):
    ''' Функция для обработки случаев совпадения имени карточки или колонки
    с уже имеющимися на доске. Такие карточки или колонки можно добавлять
    сколько угодно, просто они добавляются под именами Name_(2), Name_(3), etc.
    '''
    _DUP_FACTOR = 0
    if NEW_LINE == OLD_LINE:
        _DUP_FACTOR = 2
        _NEW_LINE_MOD = NEW_LINE + '_(' + str(_DUP_FACTOR) + ')'
    elif NEW_LINE in OLD_LINE:
        _OLD_LINE_TUP = OLD_LINE.rpartition('_(')
        if NEW_LINE == _OLD_LINE_TUP[0]:
            _LINE_NUM = _OLD_LINE_TUP[2].rstrip(')')
            if _LINE_NUM.isdecimal():
                _DUP_FACTOR = int(_LINE_NUM) + 1
            else:
                _DUP_FACTOR = 2
            _NEW_LINE_MOD = NEW_LINE + '_(' + str(_DUP_FACTOR) + ')'
        else:
            _NEW_LINE_MOD = NEW_LINE
    else:
        _NEW_LINE_MOD = NEW_LINE
    return _NEW_LINE_MOD, _DUP_FACTOR


def read():
    _ALL_LISTS_DATA = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/lists', params=AUTH_PARAMS).json()
    print('\nВ этой доске', len(_ALL_LISTS_DATA), 'колонок(ки):\n')
    for _NUM, _LIST_DATA in enumerate(_ALL_LISTS_DATA):
        _CARD_DATA = requests.get(BASE_URL.format('lists') + '/' + _LIST_DATA['id'] + '/cards', params=AUTH_PARAMS).json()
        if not _CARD_DATA:
            print('{}) \"{}\" -- нет задач'.format(str(_NUM + 1), _LIST_DATA['name']))
            continue
        else:
            print('{}) \"{}\" -- есть {} задач(и):'.format(str(_NUM + 1), _LIST_DATA['name'], str(len(_CARD_DATA))))
            for _CARD in _CARD_DATA:
                print('\t* ' + _CARD['name'])


def new_list(LIST_NAME):
    ''' Функция для создания колонки(листа) на текущей доске
    '''
    _ALL_LISTS_DATA = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/lists', params=AUTH_PARAMS).json()
    _ID_BOARD = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID, params=AUTH_PARAMS).json()['id']
    _NEW_LIST_NAME = LIST_NAME

    #####----- Обработка совпадающих имён колонок(листов) -----#####
    _DUP_MAX = 0
    for _LISTS_DATA in _ALL_LISTS_DATA:
        _DUP_NUM = find_equals(LIST_NAME, _LISTS_DATA['name'])[1]
        if _DUP_MAX < _DUP_NUM:
            _DUP_MAX = _DUP_NUM
            _NEW_LIST_NAME = LIST_NAME + '_(' + str(_DUP_MAX) + ')'

    #####----- Создание колонки(листа) на текущей доске -----#####
    requests.post(BASE_URL.format('lists'), data={'name': _NEW_LIST_NAME, 'idBoard': _ID_BOARD, **AUTH_PARAMS})


def new_card(CARD_NAME, LIST_NAME):
    ''' Функция для создания карточки в указанной колонке(листе)
    '''
    _ALL_LISTS_DATA = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/lists', params=AUTH_PARAMS).json()
    _ALL_CARDS_DATA = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/cards', params=AUTH_PARAMS).json()
    _NEW_CARD_NAME = CARD_NAME

    #####----- Обработка совпадающих имён карточек -----#####
    _DUP_MAX = 0
    for _CARDS_DATA in _ALL_CARDS_DATA:
        _DUP_NUM = find_equals(CARD_NAME, _CARDS_DATA['name'])[1]
        if _DUP_MAX < _DUP_NUM:
            _DUP_MAX = _DUP_NUM
            _NEW_CARD_NAME = CARD_NAME + '_(' + str(_DUP_MAX) + ')'

    #####----- Создание карточки в указанной колонке(листе) -----#####
    for _LIST_DATA in _ALL_LISTS_DATA:
        if _LIST_DATA['name'] == LIST_NAME:
            requests.post(BASE_URL.format('cards'), data={'name': _NEW_CARD_NAME, 'idList': _LIST_DATA['id'], **AUTH_PARAMS})
            break


def move_card(CARD_NAME, LIST_NAME):
    ''' Функция для перемещения карточки в указанную колонку(лист)
    '''
    _ALL_LISTS_DATA = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/lists', params=AUTH_PARAMS).json()
    _CARD_ID = None
    for _LIST_DATA in _ALL_LISTS_DATA:
        _LIST_CARDS = requests.get(BASE_URL.format('lists') + '/' + _LIST_DATA['id'] + '/cards', params=AUTH_PARAMS).json()
        for _CARD in _LIST_CARDS:
            if _CARD['name'] == CARD_NAME:
                _CARD_ID = _CARD['id']
                break
        if _CARD_ID:
            break
    for _LIST_DATA in _ALL_LISTS_DATA:
        if _LIST_DATA['name'] == LIST_NAME:
            requests.put(BASE_URL.format('cards') + '/' + _CARD_ID + '/idList', data={'value': _LIST_DATA['id'], **AUTH_PARAMS})
            break


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        read()
    elif sys.argv[1] == 'newlist':
        new_list(sys.argv[2])
    elif sys.argv[1] == 'newcard':
        new_card(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'movecard':
        move_card(sys.argv[2], sys.argv[3])
    else:
        print(USAGE_STR)
