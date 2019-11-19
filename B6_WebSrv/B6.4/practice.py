class CustomError(Exception):
    pass
class InvalidEmail(Exception):
    pass
class MissingAt(InvalidEmail):
    pass
class MissingDomainDot(InvalidEmail):
    pass
'''
def valid_email(email):
    parts = email.split('@')
    if len(parts) != 2:
        return False
    address, domain = parts
    if '.' not in domain:
        return False
    return True
'''
'''
def valid_email(email):
    parts = email.split('@')
    if len(parts) != 2:
        raise AttributeError('\"@\" is abcent today')
    address, domain = parts
    if '.' not in domain:
        raise AttributeError('\".\" is absent today')
    return True
'''
def valid_email(email):
    parts = email.split('@')
    if len(parts) != 2:
        raise MissingAt('\"@\" is abcent today')
    address, domain = parts
    if '.' not in domain:
        raise MissingDomainDot('\".\" is absent today')
    return True
def spam_with_exception():
    raise Exception('You can write error text here')

email = input('Enter email: ')
valid = False
try:
    valid = valid_email(email)
except AttributeError as err:
    print('Incorrect address:', err)
if valid:
    print('Correct address')
