import time

class DECORATOR1:
    def __call__(self, function):
        def wrapper(parameter, num_runs):
            RUN_COUNT = num_runs
            AVG_TIME = 0
            print('Please wait. I\'m computing', RUN_COUNT, 'iterations...')
            for COUNT in range(RUN_COUNT):
                t0 = time.time()
                function(parameter)
                t1 = time.time()
                AVG_TIME += (t1 - t0)
            AVG_TIME /= RUN_COUNT
            print('One iteration average time taken: %.5f seconds' % AVG_TIME)
        return wrapper

decorator = DECORATOR1()

@decorator
def fibonacci_row(UPPER_THRESHOLD):
    FIBO_LIST = [1, 2]
    FL = 1
    BLACKHOLE_STRING = ''
    while FIBO_LIST[FL] < UPPER_THRESHOLD:
        FIBO_LIST.append(FIBO_LIST[FL - 1] + FIBO_LIST[FL])
        FL += 1
    EVEN_SUM = 0
    for X in range(0, FL):
        if FIBO_LIST[X] %2 == 0:
            EVEN_SUM += FIBO_LIST[X]
            BLACKHOLE_STRING += 'Индекс элемента = ' + str(X) + 'Значение = ' + str(FIBO_LIST[X]) + 'Сумма = ' + str(EVEN_SUM)
    EVEN_SUM = 0
    for X in range(1, FL, 2):
        EVEN_SUM += FIBO_LIST[X]
        BLACKHOLE_STRING += 'Индекс элемента = ' + str(X) + 'Значение = ' + str(FIBO_LIST[X]) + 'Сумма = ' + str(EVEN_SUM)

# Первый параметр - верхняя граница ряда Фибоначчи
# Второй параметр - число итераций цикла вычисления ряда Фибоначчи и кое-каких сумм
fibonacci_row(1000000000000000000000, 2000)
