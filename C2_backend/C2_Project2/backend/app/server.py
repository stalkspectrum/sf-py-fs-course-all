import time
import bottle

def create_app():
    app = bottle.Bottle()
    app.config.load_config('sse_server.conf')
    app.config.setdefault('server', 'gunicorn')
    app.config.setdefault('host', 'localhost')
    app.config.setdefault('port', 8080)
    return app

app = create_app()

@app.route('/words')
def word_spammer():
    bottle.response.content_type = 'text/event-stream'
    bottle.response.cache_control = 'no-cache'
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    for word in words:
        yield 'data: %s\n\n' % word
        time.sleep(2)

if __name__ == '__main__':
    bottle.run(host='localhost', port='8080', debug=True)
    #bottle.run(app=app, host=app.config.host, port=app.config.port, server=app.config.server)
