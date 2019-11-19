from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

@route('/add')
def add():
    try:
        x = int(request.query.x)
        y = int(request.query.y)
    except ValueError:
        result = HTTPError(400, 'Incorrect parameters')
    else:
        s = x + y
        result = 'The sum of {} and {} is {}'.format(x, y, s)
    return result

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
