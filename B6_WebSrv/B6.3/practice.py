def div(x, y):
    return x / y
'''
try:
    d = div(4, 0)
    print('Result:', d)
except ZeroDivisionError as err:
    print('Error:', err)
'''
'''
try:
    alist = [1, 2, 3]
    d = div(4, alist)
    print('Result:', d)
except (ZeroDivisionError, TypeError) as err:
    print('Error:', err)
'''
try:
    alist = [1, 2, 3]
    d = div(4, alist)
    print('Result:', d)
except ZeroDivisionError:
    print('Error DIVISION BY ZERO:')
except TypeError as err:
    print('Parameter VIOLATION:', err)
