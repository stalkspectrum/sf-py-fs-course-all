import os
import random
from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

beginnings = [
    "В то же время,",
    "Вместе с тем,",
    "Коллеги,",
    "Однако,",
    "С другой стороны,",
    "Следовательно,",
    "Соответственно,",
    "Тем не менее,",
]

subjects = [
    "диджитализация бизнес-процессов",
    "контекст цифровой трансформации",
    "парадигма цифровой экономики",
    "прагматичный подход к цифровым платформам",
    "программа прорывных исследований",
    "совокупность сквозных технологий",
    "ускорение блокчейн-транзакций",
    "экспоненциальный рост Big Data",
]

verbs = [
    "выдвигает новые требования",
    "заставляет искать варианты",
    "не оставляет шанса для",
    "несет в себе риски",
    "обостряет проблему",
    "открывает новые возможности для",
    "повышает вероятность",
    "расширяет горизонты",
]

actions = [
    "бюджетного финансирования",
    "дальнейшего углубления",
    "компрометации конфиденциальных",
    "несанкционированной кастомизации",
    "нормативного регулирования",
    "практического применения",
    "синергетического эффекта",
    "универсальной коммодизации",
]

ends = [
    "внезапных открытий.",
    "волатильных активов.",
    "государственно-частных партнёрств.",
    "знаний и компетенций.",
    "нежелательных последствий.",
    "непроверенных гипотез.",
    "опасных экспериментов.",
    "цифровых следов граждан.",
]

def generate_speech():
    speech = ' '.join([
        random.choice(beginnings),
        random.choice(subjects),
        random.choice(verbs),
        random.choice(actions),
        random.choice(ends)
        ])
    return speech

@route('/')
def server_root():
    with open('index.html', 'r', encoding='UTF-8') as INDEX_FILE:
        R_OUTPUT = INDEX_FILE.read()
    return R_OUTPUT

@route('/success')
def success_dir():
    with open('success.html', 'r', encoding='UTF-8') as SUCCESS_FILE:
        S_OUTPUT = SUCCESS_FILE.read()
    return S_OUTPUT

@route('/fail')
def fail_dir():
    F_OUTPUT = HTTPError(500, 'Internal Server Error')
    return F_OUTPUT

@route('/api/generate/')
def gen_one():
    _OUTPUT_ONE = {}
    _OUTPUT_ONE['message'] = generate_speech()
    return _OUTPUT_ONE

@route('/api/generate/<number:int>')
def gen_few(number):
    _OUTPUT_FEW = {}
    _OUTPUT_FEW['messages'] = [ generate_speech() for _X in range(number) ]
    return _OUTPUT_FEW

if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), server='gunicorn', workers=2)
    else:
        run(host='localhost', port=8080, debug=True)
