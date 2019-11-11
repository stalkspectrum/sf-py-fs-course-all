krat3 = lambda NUM: NUM % 3 == 0
krat5 = lambda NUM: NUM % 5 == 0
krat7 = lambda NUM: NUM % 7 == 0
krat35 = lambda NUM: krat3(NUM) or krat5(NUM)
krat357 = lambda NUM: krat3(NUM) or krat5(NUM) or krat7(NUM)

def fizz_buzz(NAT):
    RES = ''
    if krat3(NAT):
        RES += 'Fizz'
    if krat5(NAT):
        RES += 'Buzz'
    return RES

def main():
    LAST_DIG = 10000
    SUM = 0
    TOT = 0
    for DIG in range(1, LAST_DIG):
        print(DIG, '=', fizz_buzz(DIG))
    for DIG in range(1, LAST_DIG):
        if krat35(DIG):
            SUM += DIG
    for DIG in range(1, LAST_DIG):
        if krat357(DIG):
            TOT += DIG
    print('Total FizzBuzzSum for', LAST_DIG, '=', str(SUM))
    print('Total FizzBuzzFuzzSum for', LAST_DIG, '=', str(TOT))

if __name__ == '__main__':
    main()
