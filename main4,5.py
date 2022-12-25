import random

file=open("C:\\Users\\kegn5\\Desktop\\file2.txt", "w")
text = input()
while text != "":
    file.write(text)
    file.write("\n")
    text = input()
file.close()


fileRead=open("C:\\Users\\kegn5\\Desktop\\file2.txt", "r")
k = fileRead.readline()
i = 0
while k != "":
  print("Число слов в ", i, " строке равно:")
  if k == "\n":
      print(0)
  else:
      print(len(k.split(" ")))
  i=i+1
  k = fileRead.readline()
print ("Число строк", i)

fileRead2=open("C:\\Users\\kegn5\\Desktop\\file3.txt", "r", encoding="utf8")
k = fileRead2.readline()
summa = 0
count = 0
while k != "":
    a = k.split(" ")
    summa = summa + int(a[1])
    count = count + 1
    if int(a[1])<20000:
        print(a[0])
    k = fileRead2.readline()
print(summa/count)

fileRead4=open("C:\\Users\\kegn5\\Desktop\\file4.txt", "r")
file7=open("C:\\Users\\kegn5\\Desktop\\file7.txt", "w")
k = fileRead4.readline()
while k != "":
    print(k)
    if k=='One - 1\n':
        print('один - 1')
        file7.write('один - 1')
    if k=='Two - 2\n':
        print('два - 2')
        file7.write('два - 2')
    if k=='Three - 3\n':
        print('три - 3')
        file7.write('три - 3')
    if k=='Four - 4\n':
        print('четыре - 4')
        file7.write('четыре - 4')
    k = fileRead4.readline()

file=open("C:\\Users\\kegn5\\Desktop\\file5.txt", "w")
summa = 0
for i in range(15):
    a = random.randint(10, 20)
    summa = summa + a
    file.write(str(a))
    file.write(" ")
print(summa)
file.close()


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
