#test_cases = (
#    42,
#    '',
#    [1, 2],
#    [],
#    {},
#    None,
#    0
#)
#result = []
#for entry in test_cases:
#    if entry:
#        result.append(1)
#    if entry is None:
#        result.append(0)
#print(result)

def my_func(sentinel=None, param=14):
    if sentinel is not None:
        print("Так не работает. Указывайте только именованные аргументы")
        return '000'
    return "пароли от всех секретов"
    #print('PARAM', param)

my_func(20)
#my_func(param=20)
