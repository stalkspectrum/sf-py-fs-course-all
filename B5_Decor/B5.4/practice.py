'''
def h1_wrap(func):
    def func_wrapper(param):
        return '<h1>' + func(param) + '</h1>'
    return func_wrapper
@h1_wrap
def say_hi(name):
    return 'Привет, ' + name.capitalize()
print(say_hi('арсений'))
'''
'''
def html_wrap(tag):
    def decorator(func):
        def wrap(param):
            return '<{0}>{1}</{0}>'.format(tag, func(param))
        return wrap
    return decorator
@html_wrap('h2')
def say_hi(name):
    return 'Привет, ' + name.capitalize()
print(say_hi('арсений'))
'''
def html_wrap(tag, klass=None):
    def decorator(func):
        def wrap(param):
            if klass:
                return '<{0} class=\"{2}\">{1}</{0}>'.format(tag, func(param), klass)
            else:
                return '<{0}>{1}</{0}>'.format(tag, func(param))
        return wrap
    return decorator
@html_wrap('div', klass='container')
@html_wrap('h2')
def say_hi(name):
    return 'Привет, ' + name.capitalize()
print(say_hi('арсений'))
