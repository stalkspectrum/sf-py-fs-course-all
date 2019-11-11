import time

class TimeMeter:
    def __init__(self, **ARG_DICT):
        self.FUNC = ARG_DICT['function']
        self.NUM_RUNS = ARG_DICT['num_runs']
    def __enter__(self, *args, **kwargs):
        return self
    def __exit__(self, *args, **kwargs):
        return self
    def __call__(self, *args, **kwargs):
        def wrapper(*args, **kwargs):
            AVG_TIME = 0
            print('\nPlease wait. I\'m compute', self.NUM_RUNS, 'iterations...')
            for K in range(self.NUM_RUNS):
                t0 = time.time()
                self.FUNC(*args)
                t1 = time.time()
                AVG_TIME += (t1 - t0)
            AVG_TIME /= self.NUM_RUNS
            print('Average time taken per iteration: %.6f seconds\n' % AVG_TIME)
        return wrapper(*args, **kwargs)

def fibo_sum_even(UPPER_THRESHOLD):
    '''Функция строит ряд Фибоначчи до первого числа, превысившего UPPER_THRESHOLD,
    и суммирует только чётные числа.
    '''
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

def fibo_even_sum(UPPER_THRESHOLD):
    '''Функция строит ряд Фибоначчи до первого числа, превысившего UPPER_THRESHOLD,
    и суммирует только чётные члены ряда.
    '''
    FIBO_LIST = [1, 2]
    FL = 1
    BLACKHOLE_STRING = ''
    while FIBO_LIST[FL] < UPPER_THRESHOLD:
        FIBO_LIST.append(FIBO_LIST[FL - 1] + FIBO_LIST[FL])
        FL += 1
    EVEN_SUM = 0
    for X in range(1, FL, 2):
        EVEN_SUM += FIBO_LIST[X]
        BLACKHOLE_STRING += 'Индекс элемента = ' + str(X) + 'Значение = ' + str(FIBO_LIST[X]) + 'Сумма = ' + str(EVEN_SUM)

def main():
    ''' Класс TimeMeter можно использовать в контекстном менеджере
    как измеритель среднего времени выполнения функции при
    многоразовом прогоне.
    Можно задавать и функцию параметром "function",
    и число прогонов параметром "num_runs".
    Аргументы в deco() передаются декорируемой функции
    (в данном случае UPPER_THRESHOLD)
    '''
    with TimeMeter(function=fibo_even_sum, num_runs=5000) as deco:
        deco(1000000000000000)
    with TimeMeter(function=fibo_sum_even, num_runs=2000) as deco:
        deco(5000000000000000)

if __name__ == '__main__':
    main()
