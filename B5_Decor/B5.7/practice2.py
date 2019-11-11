def fibo4M():
    FIBO_LIST = [1, 2]
    FL = 1
    while FIBO_LIST[FL] < 4000000:
        FIBO_LIST.append(FIBO_LIST[FL - 1] + FIBO_LIST[FL])
        FL += 1
    #return FIBO_LIST[FL - 1]
    return FIBO_LIST
    #return FL - 1

def fibo_even_sum():
    FIBO_LIST = [1, 2]
    FL = 1
    while FIBO_LIST[FL] < 4000000:
        FIBO_LIST.append(FIBO_LIST[FL - 1] + FIBO_LIST[FL])
        FL += 1
    EVEN_SUM = 0
    for X in range(1, FL, 2):
        EVEN_SUM += FIBO_LIST[X]
        print('Индекс элемента = {}, Значение = {}, Сумма = {}'.format(str(X), str(FIBO_LIST[X]), str(EVEN_SUM)))

def fibo_heaven_sum():
    FIBO_LIST = [1, 2]
    FL = 1
    while FIBO_LIST[FL] < 4000000:
        FIBO_LIST.append(FIBO_LIST[FL - 1] + FIBO_LIST[FL])
        FL += 1
    EVEN_SUM = 0
    for X in range(0, FL):
        if FIBO_LIST[X] %2 == 0:
            EVEN_SUM += FIBO_LIST[X]
            print('Индекс элемента = {}, Значение = {}, Сумма = {}'.format(str(X), str(FIBO_LIST[X]), str(EVEN_SUM)))

def main():
    #print(fibo4M())
    #print(fibo_even_sum())
    #fibo_even_sum()
    fibo_heaven_sum()

if __name__ == '__main__':
    main()
