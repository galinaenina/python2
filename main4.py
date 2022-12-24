def simple_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')

a = [1, 26, 48, 57, 48, 55, 258, 159, 14, 0, 148, 3, 12, 89]
c = []
for i in range(len(a) - 1):
    n = a[i]
    i += 1
    m = a[i]
    if m > n:
        c.append(m)
print(c)

list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print("Список чисел, кратных 20 или 21: ", list)

my_list = [3, 5, 8, 9, 47, 88, 59, 78, 448, 25, 47, 59, 448, 7]
print("Числа:\n", my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print("Числа без повтора:\n", new_list)

from functools import reduce
list = [i for i in range(100, 1001, 2)]
print("Чётные чисела от 100 до 1000/, включительно]:\n", list)
from itertools import count, cycle

from itertools import count
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from math import factorial
def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)
print("Факториал числа: ")
for el in factorial_gen(10):
    print(el)


