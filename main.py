a = 1
b = 2
c = 3
d = 4
f = a + b + c - d
print (f)

time_sec = int(input('Введите число: '))
hours = time_sec//3600
hours_res = (hours) if hours > 10 else ('0' + str(hours))
minutes = (time_sec % 3600)//60
minutes_res = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (time_sec % 3600) % 60
seconds_res = (seconds) if seconds > 10 else ('0' + str(seconds))
if hours > 24:
    print('Количество полученных часов превышает количество часов в сутка, скоректируйте ввод.')
else:
    print(f'Московское время: {hours_res}:{minutes_res}:{seconds_res}')

n = input('Введите число: ')
nn = int(n+n)
nnn = int(n+n+n)
n = int(n)
result = n+nn+nnn
print(result)

a = input('Введите число больше нуля:')
maxmin = max(int(x) for x in a)
print(maxmin)

plus = int(input('Введите значение прибыли: '))
minus = int(input('Введите значение издержек: '))
people = int(input('Ввдите количество работников: '))
if plus > minus:
    print('Выручка больше издержек')
    clear_plus = plus - minus
    rent = clear_plus/plus
    print('Рентабельность {} выручки {}: {:.2f}' .format('нашей','составила',rent))
    clear_for_person = float(clear_plus/people)
    print('Прибыль фирмы в расчете на одного сотрудника: %s'%clear_for_person)
else:
    print('Фирма работает в убыток')

a = int(input('Введите расстояние пробежки: '))
в = int(input('Введите максимальное расстояние пробежки: '))
day = 1
while a < b:
    a = a + (a * 0.1)
day += 1
print(f"На {day}-й день спортсмен достиг результата - не менее {b} км")

