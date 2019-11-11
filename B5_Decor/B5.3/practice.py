'''
def say_hello(name):
    return 'Привет, ' + name
say_hi = say_hello
print(say_hi('Странник'))
'''
'''
def say_hi(name):
    def get_intro(lang='ru'):
        lang = lang.lower()
        return { 'ru': 'Привет, ', 'en': 'Hello ' }[lang]
    message = get_intro() + name
    return message
print(say_hi('Странник'))
'''
'''
import random
def say_hello(name):
    return 'Привет, ' + name
def do_action(function):
    random_name = random.choice([ 'Эдгар', 'Арсений'])
    return function(random_name)
print(do_action(say_hello))
'''
'''
def compose_hello_func(name):
    def get_intro():
        return 'Привет, ' + name + '!'
    return get_intro
say_hi = compose_hello_func('Арсений')
print(say_hi())
'''
def compose_hello_func(name):
    get_intro = lambda: 'Привет, ' + name + '!'
    return get_intro
def decorate(tag):
    wrap = lambda text: '<{0}>{1}</{0}>'.format(tag, text)
    return wrap
h1_decorator = decorate('h1')
greeting = compose_hello_func('Арсений')
print(h1_decorator(greeting()))
