import json
'''
def handle_json_document(doc):
    pass
fp = open('file.txt')
try:
    document = json.load(fp)
    result = handle_json_document(document)
except json.decoder.JSONDecodeError as err:
    print('Ошибка десериализации документа JSON:', err)
finally:
    fp.close()
'''
'''
path = input('Path to TXT file: ')
print('I will try to get strings number in the file', path)
try:
    f = open(path)
except FileNotFoundError:
    print('Cannot open file.')
else:
    lines = f.readlines()
    lines_number = len(lines)
    print('Number of strings in the file:', lines_number)
    f.close()
'''
def fib(n):
    a, b = 1, 1
    for x in range(n):
        yield a
        a, b = b, a + b
def run_iterator(iterator):
    items = []
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            items.append(item)
    return items
fibonacci_sequence = fib(5)
'''
for item in fibonacci_sequence:
    print(item)
'''
'''
for i in range(6):
    item = next(fibonacci_sequence)
    print(item)
'''
for item in run_iterator(fibonacci_sequence):
    print(item)
