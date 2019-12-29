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
где N=idShort для карточки и N=id(последние 4 цифры) для колонки(листа).
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
BOARD_ID = 'Xv****b8'

#####!!!!! Вписать свои API_key и API_token !!!!!#####
AUTH_PARAMS = {
    'key': '48d9****c42b****4db9****6bc4****',
    'token': 'a03c****a88d****fb5a****8c8b****28a9****f750****bf47****28da****',
}


def find_twins(INI_LIST):
    ''' Находит в списке карточек или колонок(листов) одинаковые имена и
    отмечает их добавлением нового ключа словаря.
    '''
    _MOD_LIST = []
    _HAVE_TWINS = False
    for _DICT in INI_LIST:
        _MOD_LIST.append({**_DICT, 'twinName': False})
    for _X in range(len(_MOD_LIST) - 1):
        if not _MOD_LIST[_X]['twinName']:
            _TESTED_NAME = _MOD_LIST[_X]['name']
            for _Y in range(_X + 1, len(_MOD_LIST)):
                if _MOD_LIST[_Y]['name'] == _TESTED_NAME:
                    _MOD_LIST[_X]['twinName'] = True
                    _MOD_LIST[_Y]['twinName'] = True
                    _HAVE_TWINS = True
    return _MOD_LIST, _HAVE_TWINS


def find_equals(NEW_LINE, OLD_LINE):
    ''' Обработка случаев совпадения имени карточки или колонки с уже
    имеющимися на доске. Такие карточки или колонки можно добавлять сколько
    угодно, но теперь для уникальности они создаются под именами с добавкой
    номера в конце: Name__(2), Name__(3), Name__(4), etc.
    '''
    _DUB_FACTOR = 0
    if NEW_LINE == OLD_LINE:
        _DUB_FACTOR = 2
        _NEW_LINE_MOD = NEW_LINE + '__(' + str(_DUB_FACTOR) + ')'
    elif NEW_LINE in OLD_LINE:
        _OLD_LINE_TUP = OLD_LINE.rpartition('__(')
        if NEW_LINE == _OLD_LINE_TUP[0]:
            _LINE_NUM = _OLD_LINE_TUP[2].rstrip(')')
            if _LINE_NUM.isdecimal():
                _DUB_FACTOR = int(_LINE_NUM) + 1
            else:
                _DUB_FACTOR = 2
            _NEW_LINE_MOD = NEW_LINE + '__(' + str(_DUB_FACTOR) + ')'
        else:
            _NEW_LINE_MOD = NEW_LINE
    else:
        _NEW_LINE_MOD = NEW_LINE
    return _NEW_LINE_MOD, _DUB_FACTOR


def read():
    ''' Функция для вывода на консоль списка всех колонок(листов) и карточек
    в них для текущей доски. Если на доске встречаются карточки и/или
    колонки(листы) с одинаковыми именами, такие имена выводятся
    с добавкой "__N__", где N=idShort для карточки и N=id(последние 4 цифры)
    для колонки(листа).
    '''
    if HAVE_TWINLIST:
        print(TWINLIST_MSG)
    if HAVE_TWINCARD:
        print(TWINCARD_MSG)
    print('\nНа этой доске', len(MOD_LISTS_DATA), 'колонок(ки):\n')
    for _NUM, _LIST in enumerate(MOD_LISTS_DATA):
        _CARD_DATA = []
        for _CARD in MOD_CARDS_DATA:
            if _CARD['idList'] == _LIST['id']:
                _CARD_DATA.append(_CARD)
        if _LIST['twinName']:
            _LIST_NAME = _LIST['name'] + '__' + str(_LIST['id'][-4:]) + '__'
        else:
            _LIST_NAME = _LIST['name']
        if not _CARD_DATA:
            print('{}) \"{}\" -- нет задач'.format(str(_NUM + 1), _LIST_NAME))
            continue
        else:
            print('{}) \"{}\" -- есть {} задач(и):'.format(str(_NUM + 1), _LIST_NAME, str(len(_CARD_DATA))))
            for _CARD in _CARD_DATA:
                if _CARD['twinName']:
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
    _DUB_MAX = 0
    for _LIST in MOD_LISTS_DATA:
        _DUB_NUM = find_equals(LIST_NAME, _LIST['name'])[1]
        if _DUB_MAX < _DUB_NUM:
            _DUB_MAX = _DUB_NUM
            _NEW_LIST_NAME = LIST_NAME + '__(' + str(_DUB_MAX) + ')'

    #####----- Создание колонки(листа) на текущей доске -----#####
    requests.post(BASE_URL.format('lists'), data={'name': _NEW_LIST_NAME, 'idBoard': _ID_BOARD, **AUTH_PARAMS})


def new_card(CARD_NAME, LIST_NAME):
    ''' Функция для создания карточки в указанной колонке(листе)
    '''
    _NEW_CARD_NAME = CARD_NAME
    _LIST_ID = None
    _LISTSET = {}

    #####----- Обработка совпадающих имён карточек -----#####
    _DUB_MAX = 0
    for _CARD in MOD_CARDS_DATA:
        _DUB_NUM = find_equals(CARD_NAME, _CARD['name'])[1]
        if _DUB_MAX < _DUB_NUM:
            _DUB_MAX = _DUB_NUM
            _NEW_CARD_NAME = CARD_NAME + '__(' + str(_DUB_MAX) + ')'

    #####----- Обработка совпадающих имён колонок(листов), где создать карточку -----#####
    for _LIST in MOD_LISTS_DATA:
        if _LIST['name'] == LIST_NAME:
            if _LIST['twinName']:
                _LISTSET[_LIST['id'][-4:]] = [ _LIST['id'], _LIST['name'] ]
                print('ID=' + _LIST['id'][-4:] + ' - ' + '\"' + _LIST['name'] + '__' + _LIST['id'][-4:] + '__')
            else:
                _LIST_ID = _LIST['id']
                break
    if not _LIST_ID:
        _CHOSEN_LIST_ID = input('Из вышеприведённого списка введите ID колонки(листа), в котором надо создать карточку: ')
        _LIST_ID = _LISTSET[_CHOSEN_LIST_ID][0]

    #####----- Создание карточки в указанной колонке(листе) -----#####
    requests.post(BASE_URL.format('cards'), data={'name': _NEW_CARD_NAME, 'idList': _LIST_ID, **AUTH_PARAMS})


def move_card(CARD_NAME, LIST_NAME):
    ''' Функция для перемещения карточки в указанную колонку(лист). Если на
    доске есть несколько карточек с таким именем, предлагает выбрать конкретную
    карточку по ID из списка. Если есть несколько колонок(листов)
    с одинаковыми именами, аналогично предлагает выбрать конкретную
    колонку(лист) по ID из списка, куда перемещать карточку.
    '''
    _CARD_ID = None
    _LIST_ID = None
    _CARDSET = {}
    _LISTSET = {}

    #####----- Обработка совпадающих имён карточек -----#####
    for _CARD in MOD_CARDS_DATA:
        if _CARD['name'] == CARD_NAME:
            if _CARD['twinName']:
                for _LIST in MOD_LISTS_DATA:
                    if _LIST['id'] == _CARD['idList']:
                        _CARDSET[_CARD['idShort']] = [ _CARD['id'], _CARD['name'], _LIST['id'], _LIST['name'] ]
                        break
                print('ID=' + str(_CARD['idShort']) + ' - ' + '\"' + _CARD['name'] + '__' + str(_CARD['idShort']) + '__\" в колонке \"' + _CARDSET[_CARD['idShort']][3] + '\"')
            else:
                _CARD_ID = _CARD['id']
                break
    if not _CARD_ID:
        _CHOSEN_CARD_ID = int(input('Из вышеприведённого списка введите ID карточки (только число), которую надо переместить: '))
        _CARD_ID = _CARDSET[_CHOSEN_CARD_ID][0]

    #####----- Обработка совпадающих имён колонок(листов) -----#####
    for _LIST in MOD_LISTS_DATA:
        if _LIST['name'] == LIST_NAME:
            if _LIST['twinName']:
                _LISTSET[_LIST['id'][-4:]] = [ _LIST['id'], _LIST['name'] ]
                print('ID=' + _LIST['id'][-4:] + ' - ' + '\"' + _LIST['name'] + '__' + _LIST['id'][-4:] + '__')
            else:
                _LIST_ID = _LIST['id']
                break
    if not _LIST_ID:
        _CHOSEN_LIST_ID = input('Из вышеприведённого списка введите ID колонки(листа), в которой надо переместить карточку: ')
        _LIST_ID = _LISTSET[_CHOSEN_LIST_ID][0]

    #####----- Перемещение карточки в указанную колонку(лист) -----#####
    requests.put(BASE_URL.format('cards') + '/' + _CARD_ID + '/idList', data={'value': _LIST_ID, **AUTH_PARAMS})


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
