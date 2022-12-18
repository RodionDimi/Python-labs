# Задание №1
n = int(input('Введите длину списка: '))
a = [0] * n
for i in range(0, n):
    a[i] = int(input())
l = len(a)
if l % 2 == 0:
    b = [0] * (l//2)
else:
    b = [0] * ((l//2)+1)
k = 0
for i in range(0, n):
    if i % 2 == 0:
        b[k] = a[i]
        k += 1
    else:
        continue
print(b)

# Задание №2
n = int(input('Введите длину списка: '))
a = [0] * n
for i in range(0, n):
    a[i] = int(input())
k = 0
for i in range(1, n):
    if a[i] > a[i-1]:
        k += 1
    else:
        continue
b = [0] * k
m = 0
for i in range(1, n):
    if a[i] > a[i-1]:
        b[m] = a[i]
        m += 1
print(b)

# Задание №3
n = int(input('Введите длину списка: '))
a = [0] * n
for i in range(0, n):
    a[i] = int(input())
print(a)
m = max(a)
n = min(a)
k = a.index(m)
l = a.index(n)
a[l] = a[k]
a[k] = n
print(a)

# Задание №4
n = int(input('Введите количество значений:'))
a = {}
b = [0] * 2 * n
for i in range(0,2 * n, 2):
    b[i] = input('Введите ключ:')
for i in range(1, 2 * n, 2):
    b[i] = input('Введите значение:')
for i in range(0, 2 * n, 2):
    a[b[i]] = b[i+1]
print(a)
h = input('Введите ключ, значение которого хотите получить:')
print(a[h])
