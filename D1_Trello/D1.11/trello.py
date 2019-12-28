'''!!!!!!!!!! USAGE: !!!!!!!!!!
Вывод всех колонок с числом и списком карточек в каждой колонке:
    python trello.py
Создать новую колонку(лист) List_Name на доске:
    python trello.py newlist "List_Name"
Создать карточку Card_Name в колонке(листе) List_Name:
    python trello.py newcard "Card_Name" "List_Name"
Переместить карточку Card_Name в колонку(лист) List_Name:
    python trello.py movecard "Card_Name" "List_Name"

Если на доске встречаются карточки и/или колонки(листы) с одинаковыми
именами, такие имена выводятся с добавкой "__N__",
где N=idShort для карточки и N=id(последние 4 цифры) для колонки(листа).На доске встречаются карточки и/или колонки(листы) с одинаковыми\n\
именами. Такие имена выводятся с добавкой \"__N__\",\n\
где N=idShort для карточки и N=id(последние 4 цифры) для колонки(листа).\n\
'''

import sys
import requests

USAGE_MSG = '\n!!!!!!!!!! USAGE: !!!!!!!!!!\n\
Вывод всех колонок с числом и списком карточек в каждой колонке:\n\
\tpython trello.py\n\n\
Создать новую колонку(лист) List_Name на доске:\n\
\tpython trello.py newlist \"List_Name\"\n\n\
Создать карточку Card_Name в колонке(листе) List_Name:\n\
\tpython trello.py newcard \"Card_Name\" \"List_Name\"\n\n\
Переместить карточку Card_Name в колонку(лист) List_Name:\n\
\tpython trello.py movecard \"Card_Name\" \"List_Name\"\n\
============================\n'

TWINLIST_MSG = '\n!!!!!!!!!! WARNING !!!!!!!!!!\n\
На доске встречаются колонки(листы) с одинаковыми именами. Такие имена\n\
выводятся с добавкой \"__N__\", где N=id колонки (последние 4 цифры).\n\
=============================\n'

TWINCARD_MSG = '\n!!!!!!!!!! WARNING !!!!!!!!!!\n\
На доске встречаются карточки с одинаковыми именами. Такие имена выводятся\n\
с добавкой \"__N__\", где N=idShort карточки.\n\
=============================\n'

BASE_URL = 'https://api.trello.com/1/{}'

#####!!!!! Вписать свой Board_ID !!!!!#####
BOARD_ID = 'XvaZ3Sb8'

#####!!!!! Вписать свои API_key и API_token !!!!!#####
AUTH_PARAMS = {
    'key': '48d929e1c42b6c714db9370c6bc474eb',
    'token': 'a03c20cba88d5743fb5a691f8c8b76d128a9a4b2f750be86bf47412528da0d5e',
}


def find_twins(ini_list):
    ''' Находит в списке карточек или колонок(листов) одинаковые имена и
    отмечает их добавлением нового ключа словаря.
    '''
    _mod_list = []
    _have_twins = False
    for _dict in ini_list:
        _mod_list.append({**_dict, 'twin': False})
    for _x in range(len(_mod_list) - 1):
        if not _mod_list[_x]['twin']:
            _tested_name = _mod_list[_x]['name']
            for _y in range(_x + 1, len(_mod_list)):
                if _mod_list[_y]['name'] == _tested_name:
                    _mod_list[_x]['twin'] = True
                    _mod_list[_y]['twin'] = True
                    _have_twins = True
    return _mod_list, _have_twins


def find_equals(new_line, old_line):
    ''' Обработка случаев совпадения имени карточки или колонки с уже
    имеющимися на доске. Такие карточки или колонки можно добавлять сколько
    угодно, но теперь для уникальности они создаются под именами с добавкой
    номера в конце: Name__(2), Name__(3), Name__(4), etc.
    '''
    _dub_factor = 0
    if new_line == old_line:
        _dub_factor = 2
        _new_line_mod = new_line + '__(' + str(_dub_factor) + ')'
    elif new_line in old_line:
        _old_line_tuple = old_line.rpartition('__(')
        if new_line == _old_line_tuple[0]:
            _line_dubnum = _old_line_tuple[2].rstrip(')')
            if _line_dubnum.isdecimal():
                _dub_factor = int(_line_dubnum) + 1
            else:
                _dub_factor = 2
            _new_line_mod = new_line + '__(' + str(_dub_factor) + ')'
        else:
            _new_line_mod = new_line
    else:
        _new_line_mod = new_line
    return _new_line_mod, _dub_factor


def read():
    if HAVE_TWINLIST:
        print(TWINLIST_MSG)
    if HAVE_TWINCARD:
        print(TWINCARD_MSG)
    print('\nНа этой доске', len(MOD_LISTS_DATA), 'колонок(ки):\n')
    for _NUM, _LIST_DATA in enumerate(MOD_LISTS_DATA):
        _CARD_DATA = []
        for _CARD in MOD_CARDS_DATA:
            if _CARD['idList'] == _LIST_DATA['id']:
                _CARD_DATA.append(_CARD)
        if _LIST_DATA['twin']:
            _LIST_NAME = _LIST_DATA['name'] + '__' + str(_LIST_DATA['id'][-4:] + '__')
        else:
            _LIST_NAME = _LIST_DATA['name']
        if not _CARD_DATA:
            print('{}) \"{}\" -- нет задач'.format(str(_NUM + 1), _LIST_NAME))
            continue
        else:
            print('{}) \"{}\" -- есть {} задач(и):'.format(str(_NUM + 1), _LIST_NAME, str(len(_CARD_DATA))))
            for _CARD in _CARD_DATA:
                if _CARD['twin']:
                    _CARD_NAME = _CARD['name'] + '__' + str(_CARD['idShort']) + '__'
                else:
                    _CARD_NAME = _CARD['name']
                print('\t* ' + _CARD_NAME)


def new_list(LIST_NAME):
    ''' Функция для создания колонки(листа) на текущей доске
    '''
    _ID_BOARD = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID, params=AUTH_PARAMS).json()['id']
    _NEW_LIST_NAME = LIST_NAME

    #####----- Обработка совпадающих имён колонок(листов) -----#####
    _DUP_MAX = 0
    for _LISTS_DATA in INI_LISTS_DATA:
        _DUP_NUM = find_equals(LIST_NAME, _LISTS_DATA['name'])[1]
        if _DUP_MAX < _DUP_NUM:
            _DUP_MAX = _DUP_NUM
            _NEW_LIST_NAME = LIST_NAME + '__(' + str(_DUP_MAX) + ')'

    #####----- Создание колонки(листа) на текущей доске -----#####
    requests.post(BASE_URL.format('lists'), data={'name': _NEW_LIST_NAME, 'idBoard': _ID_BOARD, **AUTH_PARAMS})


def new_card(CARD_NAME, LIST_NAME):
    ''' Функция для создания карточки в указанной колонке(листе)
    '''
    _NEW_CARD_NAME = CARD_NAME

    #####----- Обработка совпадающих имён карточек -----#####
    _DUP_MAX = 0
    for _CARDS_DATA in INI_CARDS_DATA:
        _DUP_NUM = find_equals(CARD_NAME, _CARDS_DATA['name'])[1]
        if _DUP_MAX < _DUP_NUM:
            _DUP_MAX = _DUP_NUM
            _NEW_CARD_NAME = CARD_NAME + '__(' + str(_DUP_MAX) + ')'

    #####----- Создание карточки в указанной колонке(листе) -----#####
    for _LIST_DATA in INI_LISTS_DATA:
        if _LIST_DATA['name'] == LIST_NAME:
            requests.post(BASE_URL.format('cards'), data={'name': _NEW_CARD_NAME, 'idList': _LIST_DATA['id'], **AUTH_PARAMS})
            break


def move_card(CARD_NAME, LIST_NAME):
    ''' Функция для перемещения карточки в указанную колонку(лист)
    '''
    _CARD_ID = None
    for _LIST_DATA in INI_LISTS_DATA:
        _LIST_CARDS = requests.get(BASE_URL.format('lists') + '/' + _LIST_DATA['id'] + '/cards', params=AUTH_PARAMS).json()
        for _CARD in _LIST_CARDS:
            if _CARD['name'] == CARD_NAME:
                _CARD_ID = _CARD['id']
                break
        if _CARD_ID:
            break
    for _LIST_DATA in INI_LISTS_DATA:
        if _LIST_DATA['name'] == LIST_NAME:
            requests.put(BASE_URL.format('cards') + '/' + _CARD_ID + '/idList', data={'value': _LIST_DATA['id'], **AUTH_PARAMS})
            break


if __name__ == '__main__':
    INI_LISTS_DATA = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/lists', params=AUTH_PARAMS).json()
    INI_CARDS_DATA = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/cards', params=AUTH_PARAMS).json()
    MOD_LISTS_DATA, HAVE_TWINLIST = find_twins(INI_LISTS_DATA)
    MOD_CARDS_DATA, HAVE_TWINCARD = find_twins(INI_CARDS_DATA)
    if len(sys.argv) <= 1:
        read()
    elif sys.argv[1] == 'newlist':
        new_list(sys.argv[2])
    elif sys.argv[1] == 'newcard':
        new_card(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'movecard':
        move_card(sys.argv[2], sys.argv[3])
    else:
        print(USAGE_MSG)
