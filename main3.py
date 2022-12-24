def s_calc():
    try:
        a = float(input("Укажите делимое: "))
        b = float(input("Укажите число делителя, не равное 0: "))
        c = a/b
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return (c)
c = s_calc()
print(c)

def personal_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')
personal_data(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),)

def my_func(number1, number2, number3):
    print(f'Сумма двух наибольших чисел равна: {number1 + number2 + number3 - min([number1, number2, number3])}')
my_func(
    int(input('Число 1:')),
    int(input('Число 2:')),
    int(input('Число 3:')),)

def s_calc():
    x = float(input(" Ведите число больше 0: "))
    y = float(input(" Введите число меньше 0: "))
    c = x**y
    return (c)
c = s_calc()
print(c)

def calculate_sum(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag
general_sum = 0
while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = calculate_sum(*numbers_string)
    general_sum += sum
    print(f'сумма {general_sum}')
    if stop_flag:
        break

def int_func():
    x = input("Ведите слова буквами маленького регистра: ")
    return x.title()
print(int_func())

