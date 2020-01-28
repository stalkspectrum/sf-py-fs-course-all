import bottle
from app.server import app

if __name__ == '__main__':
    bottle.run(host='localhost', port='8080', debug=True)
    #bottle.run(app, host=app.config.host, port=app.config.port, server=app.config.server)
