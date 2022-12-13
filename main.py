number = 44444
text = 'задание'
mix = 3, 4, 7, 'решение'
print(type(number))
print(type(text))
print(type(mix))

s = [int(i) for i in input("Введите числа через пробел: ").split(" ")]
for i in range(1, len(s)-1, 2):
    s[i-1], s[i] = s[i], s[i-1]
print(''.join([str(i) for i in s]))

m = int(input("Введите номер месяца: "))
x = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8),'Осень': (9, 10, 11)}
[print(a) for a, b in x.items() if m in b]

list = input('Введите слова через пробел: ').split()
for i, el in enumerate(list):
    print(i, el[0:10])

my_list = [5, 4, 3, 2, 1]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (000 - выход): "))
while digit != 000:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число (000 - выход) "))





