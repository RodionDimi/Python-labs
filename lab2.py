# Задание №1
a = True
b = False
print (a and b)
print ((a and b) or b)
print ((a and b) or not (a and b))
print (a and b or not (a or b) or b)
print (b and b or not a and (a or b or a) or not (a or b))
print(1 << 2)
print(1 & 0 | 1 >> 1)
print(1 & 0 | 1 >> 0)
print(0b101 & 0b111 ^ 0b111 | 0b010)

# Задание №2
a = int(input("Введите первое число = "))
b = int(input("Введите второе число = "))
if a > b :
    print(b,"- Наименьшее число")
elif a == b :
    print("Они равны")
else :
    print(a,"- Наименьшее число")

# Задание №3
a = input("First number = ")
b = input("Second number = ")
c = input("Third number = ")
if a > b and a > c :
    print(a,"- the biggest number")
elif b > a and b > c :
    print(b,"- the biggest number")
elif c > a and c > b :
    print(c,"- the biggest number")
else :
    print("There are some equal numbers")

# Задание №4
a = input("First number = ")
b = input("Second number = ")
c = input("Third number = ")
z = {a,b,c}
print(len(z),"- amount of unique numbers")
