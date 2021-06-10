"""Урок 9. Знакомство с Python
3. Реализовать базовый класс Worker (работник):
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров."""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return " ".join((self.name, self.surname))

    def get_total_income(self):
        return sum(self._income.values())

    def show_info(self):
        print(f'\nИнформация по сотруднику {self.get_full_name()}:\n'
              f'- должность: {self.position}\n'
              f'- доход в мес.: {self.get_total_income()}$ '
              f'(оклад - {self._income["wage"]}$, '
              f'премия - {self._income["bonus"]}$)')


if __name__ == "__main__":
    worker = Position("Homer", "Simpson", "base worker", {'wage': 300,
                                                          'bonus': 100})
    boss = Position("Montgomery", "Burns", "big boss", {'wage': 10000,
                                                        'bonus': 8000})
    worker.show_info()
    boss.show_info()
