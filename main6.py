from time import sleep
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def working(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(5)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            i += 1
t = TrafficLight()
t.working()

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия дороги неободимо {round(asphalt_mass)} кг асфальта')

r = Road(1000, 10)
r.asphalt_mass()


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

p = Position('Иван', 'Иванов', 'педагог', '55000', '5000')
print(p.get_full_name(), p.get_total_income())


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'\nThe {self.name} has stopped.'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def show_speed(self):
        return f'\nYour speed is {self.speed}'

class TownCar(Car):
    def show_speed(self):
        def __init__(self, speed, color, name, is_police):
             super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    pass

town = TownCar('AudiQ5', 110, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())


