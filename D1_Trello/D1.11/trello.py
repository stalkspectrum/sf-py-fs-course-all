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
BOARD_ID = 'XvaZ3Sb8'                                                               # Вписать свой Board_ID
AUTH_PARAMS = {
    'key': '48d929e1c42b6c714db9370c6bc474eb',                                      # Вписать свой API_key
    'token': 'a03c20cba88d5743fb5a691f8c8b76d128a9a4b2f750be86bf47412528da0d5e',    # Вписать свой API_token
}

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
    _ALL_LISTS_DATA = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/lists', params=AUTH_PARAMS).json()
    #_ID_BOARD = _ALL_LISTS_DATA[0]['idBoard']
    _ID_BOARD = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID, params=AUTH_PARAMS).json()['id']
    requests.post(BASE_URL.format('lists'), data={'name': LIST_NAME, 'idBoard': _ID_BOARD, **AUTH_PARAMS})

def new_card(CARD_NAME, LIST_NAME):
    #_ALL_CARDS_DATA = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/cards', params=AUTH_PARAMS).json()
    #for _CARDS_DATA in _ALL_CARDS_DATA:
        #if _CARDS_DATA['name'] == CARD_NAME:
            #pass
    _ALL_LISTS_DATA = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/lists', params=AUTH_PARAMS).json()
    for _LIST_DATA in _ALL_LISTS_DATA:
        if _LIST_DATA['name'] == LIST_NAME:
            requests.post(BASE_URL.format('cards'), data={'name': CARD_NAME, 'idList': _LIST_DATA['id'], **AUTH_PARAMS})
            break

def move_card(CARD_NAME, LIST_NAME):
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
