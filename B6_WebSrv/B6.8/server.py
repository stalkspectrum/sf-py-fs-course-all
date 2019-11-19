from bottle import route
from bottle import run
from bottle import HTTPError

def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a
@route('/hello')
def hello_world():
    return 'Hello World!'
@route('/upper/<param>')
def upper(param):
    return param.upper()
@route('/fib/<n:int>')
def fib_handler(n):
    result = fib(n)
    return str(result)
@route('/modify/<param>/<method>')
def modify(param, method):
    if method == 'upper':
        result = param.upper()
    elif method == 'lower':
        result = param.lower()
    elif method == 'title':
        result = param.title()
    else:
        result = HTTPError(400, 'Incorrect \"method\" value')
    return result

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
