from http import cookies
from datetime import timedelta, datetime as dt

c = cookies.SimpleCookie()

c['partial_cookie'] = 'cookie_value'
c['partial_cookie']['path'] = '/usr/local'
c['partial_cookie']['domain'] = 'ssszone.ru'
c['partial_cookie']['secure'] = True

c['cookie_expiring_age'] = 'Off after 5 min'
c['cookie_expiring_age']['max-age'] = 300

c['expires_at_time'] = 'cookie_value'
time_to_live = timedelta(hours=1)
expiration = (dt(2020, 10, 10, 19, 30, 15) + time_to_live)
c['expires_at_time']['expires'] = expiration.strftime('%a, %d %b %Y %H:%M:%S')

print(c.js_output())
