import sentry_sdk
from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://6bd2d39cdb25407385f1dcfc9c40527d@sentry.io/1850908",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/')
def index():
    raise RuntimeError('There is an error!')
    return

app.run(host='localhost', port=8080)
