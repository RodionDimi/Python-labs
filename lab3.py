def Sum(i):
    print('введите числа')
    q = [int(input()) for x in range(i)]
    s = 0
    for n in range(i):
        s += q[n]
    print('Сумма чисел равна:')
    print(s)


def Zero(i):
    print('введите числа')
    q = [int(input()) for x in range(i)]
    k = 0
    for n in range(i):
        if q[n] == 0:
            k += 1
    print('Количество чисел, равных нулю: ' + str(k))


def Ladder(n):
    for i in range(1, n+1):
        q = list(range(1, i+1))
        print(q)


def Pyramid(n):
    for i in range(1 , n+1):
        print(' ' * (n - i), end = '')
        print(*range(1, i), *range(1, i+1)[::-1], sep = '')
