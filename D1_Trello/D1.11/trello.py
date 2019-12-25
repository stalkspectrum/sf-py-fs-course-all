import sys
import requests

auth_params = {
    'key': '48d929e1c42b6c714db9370c6bc474eb',
    'token': 'a03c20cba88d5743fb5a691f8c8b76d128a9a4b2f750be86bf47412528da0d5e',
}

base_url = 'https://api.trello.com/1/{}'
#URL = 'https://trello.com/b/XvaZ3Sb8/created-with-pythoncli'
#board_id = '5e00c85889c386305ff34cb8'
board_id = 'XvaZ3Sb8'

def read():
    all_lists_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
    print('\nВ этой доске', len(all_lists_data), 'колонки:\n')
    _num = 0
    for column in all_lists_data:
        task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()
        _num += 1
        if not task_data:
            print(str(_num) + ') \"' + column['name'] + '\" -- нет задач')
            continue
        else:
            print(str(_num) + ') \"' + column['name'] + '\" -- есть ' + str(len(task_data)) + ' задач(и):')
            for task in task_data:
                print('\t* ' + task['name'])

def create(name, column_name):
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
    #all_cards_data = requests.get(base_url.format('boards') + '/' + board_id + '/cards', params=auth_params).json()
    for column in column_data:
        if column['name'] == column_name:
            requests.post(base_url.format('cards'), data={'name': name, 'idList': column['id'], **auth_params})
            break

def move(name, column_name):
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
    task_id = None
    for column in column_data:
        column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()
        for task in column_tasks:
            if task['name'] == name:
                task_id = task['id']
                break
        if task_id:
            break
    for column in column_data:
        if column['name'] == column_name:
            requests.put(base_url.format('cards') + '/' + task_id + '/idList', data={'value': column['id'], **auth_params})
            break

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        read()
    elif sys.argv[1] == 'create':
        create(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'move':
        move(sys.argv[2], sys.argv[3])
