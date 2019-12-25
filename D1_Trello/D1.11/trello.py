import sys
import requests

AUTH_PARAMS = {
    'key': '48d9****c42b****4db9****6bc4****',                                      # Write your API_KEY here
    'token': 'a03c****a88d****fb5a****8c8b****28a9****f750****bf47****28da****',    # Write your API_TOKEN here
}

BASE_URL = 'https://api.trello.com/1/{}'
BOARD_ID = 'Xv****b8'                                                               # Write your BOARD_ID here

def read():
    all_lists_data = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/lists', params=AUTH_PARAMS).json()
    print('\nВ этой доске', len(all_lists_data), 'колонки:\n')
    _num = 0
    for column in all_lists_data:
        task_data = requests.get(BASE_URL.format('lists') + '/' + column['id'] + '/cards', params=AUTH_PARAMS).json()
        _num += 1
        if not task_data:
            print(str(_num) + ') \"' + column['name'] + '\" -- нет задач')
            continue
        else:
            print(str(_num) + ') \"' + column['name'] + '\" -- есть ' + str(len(task_data)) + ' задач(и):')
            for task in task_data:
                print('\t* ' + task['name'])

def create(name, column_name):
    column_data = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/lists', params=AUTH_PARAMS).json()
    #all_cards_data = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/cards', params=AUTH_PARAMS).json()
    for column in column_data:
        if column['name'] == column_name:
            requests.post(BASE_URL.format('cards'), data={'name': name, 'idList': column['id'], **AUTH_PARAMS})
            break

def move(name, column_name):
    column_data = requests.get(BASE_URL.format('boards') + '/' + BOARD_ID + '/lists', params=AUTH_PARAMS).json()
    task_id = None
    for column in column_data:
        column_tasks = requests.get(BASE_URL.format('lists') + '/' + column['id'] + '/cards', params=AUTH_PARAMS).json()
        for task in column_tasks:
            if task['name'] == name:
                task_id = task['id']
                break
        if task_id:
            break
    for column in column_data:
        if column['name'] == column_name:
            requests.put(BASE_URL.format('cards') + '/' + task_id + '/idList', data={'value': column['id'], **AUTH_PARAMS})
            break

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        read()
    elif sys.argv[1] == 'create':
        create(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'move':
        move(sys.argv[2], sys.argv[3])
