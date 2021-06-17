"""Урок 9. Знакомство с Python
4. Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
к атрибутам, выведите результат. Вызовите методы и покажите результат."""

RED_COL = '\033[31m'
GRN_COL = '\033[32m'
BLUE_COL = '\033[34m'
CLR_COL = '\033[0m'


class Car:

    def __init__(self, name, color, speed=0, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        self.direction = ''

    def go(self):
        print(f'Машина {self.name} (цвет {self.color}) - поехала')

    def stop(self):
        print(f'Машина {self.name} (цвет {self.color}) - остановилась')

    def turn(self, direction):

        if direction not in ('лево', 'право', 'разворот'):
            print(f'{RED_COL}Нет такого направления "{direction}"!{CLR_COL}')
            return
        self.direction = direction
        print(f'Машина {self.name} (цвет "{self.color}") - повернула на'
              f' {self.direction}.')

    def show_speed(self):
        return self.speed


class TownCar(Car):
    SPEED_LIMIT = 60  # ограничение скорости, км/ч

    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self):
        if self.speed <= self.SPEED_LIMIT:
            return f'Скорость {GRN_COL}{self.speed} км/ч{CLR_COL} - в рамках ' \
                   f'скоростного режима!\n'
        return f'Текущая скорость {RED_COL}{self.speed} км/ч{CLR_COL} - ' \
               f'превышение на {RED_COL}{self.speed - self.SPEED_LIMIT} км/ч ' \
               f'- притормози!{CLR_COL}\n'


class WorkCar(Car):
    SPEED_LIMIT = 40  # ограничение скорости, км/ч

    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self):
        if self.speed <= self.SPEED_LIMIT:
            return f'Скорость {GRN_COL}{self.speed} км/ч{CLR_COL}.\n' \
                   f'Дело служебное - кто понял жизнь - тот не торопится!\n'
        return f'Текущая скорость {RED_COL}{self.speed} км/ч{CLR_COL} - ' \
               f'превышение на {RED_COL}{self.speed - self.SPEED_LIMIT} км/ч ' \
               f'- сбавь обороты!{CLR_COL}\n'


class SportCar(Car):
    SPEED_LIMIT = 120  # ограничение скорости, км/ч

    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self):
        if self.speed <= self.SPEED_LIMIT:
            return f'Скорость {GRN_COL}{self.speed} км/ч{CLR_COL}.\n' \
                   f'В пределах разумного...\n'
        return f'Текущая скорость {RED_COL}{self.speed} км/ч{CLR_COL} - ' \
               f'превышение на {RED_COL}{self.speed - self.SPEED_LIMIT} км/ч ' \
               f'- надавить тапку в пол хочется - понять можно!{CLR_COL}\n'


class PoliceCar(Car):

    def __init__(self, name):
        super().__init__(name, f"{RED_COL}Полиц{BLUE_COL}ейский "
                               f"{RED_COL}Шаб{BLUE_COL}лон{CLR_COL}",
                         is_police=True)

    def show_speed(self):
        return f'Текущая скорость {GRN_COL}{self.speed} км/ч{CLR_COL} - ' \
               f'никаких ограничений - главное про спецсигналы не забыть!\n'


if __name__ == '__main__':
    town_car1 = TownCar(f'{GRN_COL}Renault Logan{CLR_COL}',
                        f'{GRN_COL}зеленый{CLR_COL}')
    work_car1 = WorkCar('Gazelle', 'белый')
    sport_car1 = SportCar(f'{RED_COL}Lamborghini Diablo{CLR_COL}',
                          f'{RED_COL}красный{CLR_COL}')
    police_car1 = PoliceCar(f'{RED_COL}Dod{BLUE_COL}ge {RED_COL}Inter{BLUE_COL}'
                            f'pid{CLR_COL}')

    # test block
    speeds = (35, 55, 75, 130)
    turns = ('лево', 'право', 'разворот', 'лажа')
    cars = (town_car1, work_car1, sport_car1, police_car1)

    for car in cars:
        car.go()
        for turn in turns:
            car.turn(turn)
        car.stop()

        for test_speed in speeds:
            car.speed = test_speed
            print(f'Автомобиль {car.name}, цвет {car.color}')
            print(car.show_speed())
