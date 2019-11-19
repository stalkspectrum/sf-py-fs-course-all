class InvalidEmail(Exception):
    pass
class MissingAt(InvalidEmail):
    pass
class MissingDomainDot(InvalidEmail):
    pass
def valid_email(email):
    assert isinstance(email, str), 'Incorrect type. Expecting string.'
    parts = email.split('@')
    if len(parts) != 2:
        raise MissingAt('\"@\" is absent today')
    address, domain = parts
    if '.' not in domain:
        raise MissingDomainDot('\".\" is absent today')
    return True

email = input('Enter email: ')
valid = False
try:
    valid = valid_email(email)
except AttributeError as err:
    print('Incorrect address:', err)
if valid:
    print('Correct address')
