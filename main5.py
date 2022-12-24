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


# Задание 4го урока

simple_calc def():
    float = x(input('Введите количество отработанных часов : '))
    floaty = y(input('Введите суммы оплаты труда за 1 час : '))
    float = cпоплавок(input('Укажите размер премии - '))
    оплата  = x * y
    возврат  оплаты  + c
print(f'Размер заработной платы составил: {simple_calc() }')

= a [1, 26, 48, 57, 48, 55, 258, 159, 14, 0, 148, 3, 12, 89]
= c []
диапазон  в  i  для (len(a) -1 ):
    a = n[i]
    я += 1
    a = m[i]
    n > m , если:
        c.добавить(m)
печать(c)

= список [i  для  i  в  диапазоне (20, 240), если  i % 20 == 0  или  i % 21 == 0]
print("Список чисел, кратных 20 или 21: ", list)

= мой список [3, 5, 8, 9, 47, 88, 59, 78, 448, 25, 47, 59, 448, 7]
print("Числа:\n", my_list)
= new_list [i  для  i  в  my_list , если  my_list.count(i) == 1]
print("Числа без повтора:\n", new_list)

из  functools  импорт  сокращается
= список [i  для  i  в  диапазоне (100, 1001, 2)]
print("Чётные чисела от 100 до 1000/, включительно]:\n", list)
считать , импортировать  итерационные инструменты  из, цикл

из  itertools  количество импортируемых  файлов
количество  в  el  для (3):
    10 > el , если:
        перерыв
    ещё:
        печать(el)

из  математического  импортного  факториала
factorial_gen  определение (n):
    диапазон  в  i  для (n):
        вывести(i, end='! = ')
        факториальная  доходность(i)
print("Факториал числа: ")
факториал_ген  в  el  для(10):
    печать(el)
