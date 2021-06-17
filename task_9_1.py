"""Урок 9. Знакомство с Python
1. Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт"""

from os import system
from time import sleep

RED_COL = '\033[31m'
YEL_COL = '\033[33m'
GRN_COL = '\033[32m'
CLR_COL = '\033[0m'


class TrafficLight:
    __color = 'red'

    def __init__(self, color='red'):
        __color = color
        self.time_red = 7
        self.time_yel = 2
        self.time_grn = 10

    def running(self, color):
        if self.__color == 'red':
            print(f'Текущий цвет светофора: {RED_COL}{self.__color}{CLR_COL}')
            sleep(self.time_red)
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            print(f'Текущий цвет светофора: {YEL_COL}{self.__color}{CLR_COL}')
            sleep(self.time_yel)
            self.__color = 'green'
        elif self.__color == 'green':
            print(f'Текущий цвет светофора: {GRN_COL}{self.__color}{CLR_COL}')
            sleep(self.time_grn)
            self.__color = 'red'
        else:
            print(f'Странный цвет светофора: '
                  f'{RED_COL_COL}{self.__color}{CLR_COL}!')


if __name__ == '__main__':
    my_traf_light = TrafficLight()
    for step in range(10):
        my_traf_light.running('green')
        system('cls')
