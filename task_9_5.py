"""Урок 9. Знакомство с Python
5. Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для
каждого экземпляра."""

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}: Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}: Подрасту и стану Паркером!')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}: Да не оскудеет рука точащая...')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}: Надеюсь - ты знаешь, что делаешь...')


if __name__ == "__main__":
    buble_pen = Pen('Buble Pen')
    kohinoor = Pencil('Kohinoor HB')
    big_bold_handle = Handle('Big Bold Handle')
    base_stationery = Stationery('Base Stationery')
    stationerys = (buble_pen, kohinoor, big_bold_handle, base_stationery)
    for stationery in stationerys:
        stationery.draw()
