import logging

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename='access.log')
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

class OnlyInfoFilter:
    def filter(self, logRecord):
        return logRecord.levelno == logging.INFO

handler.addFilter(OnlyInfoFilter())
LOG.addHandler(handler)

from bottle import route, run, request

@route('/')
def index():
    LOG.info(request.headers.get("User-Agent"))
    return

run(host='localhost', port=8080)
