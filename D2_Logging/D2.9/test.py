import time
import sentry_sdk

#sentry_sdk.init("https://28c195fe195c45a8945de3ef9c26956f@sentry.io/1850837") 0.13.2
sentry_sdk.init("https://6bd2d39cdb25407385f1dcfc9c40527d@sentry.io/1850908")

division_by_zero = 1 / 0
time.sleep(10)
