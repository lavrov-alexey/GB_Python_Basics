"""Урок 10. Объектно-ориентированное программирование. Продвинутый уровень
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определённое название. К типам одежды в этом проекте относятся пальто и
костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
(для костюма). Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на
этом уроке знания. Реализовать абстрактные классы для основных классов проекта
и проверить работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cost_cloth(self):
        """обязательный для потомков Clothes метод подсчета расхода ткани"""
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def cost_cloth(self):
        """вычисляет расход ткани на пальто"""
        return self.size / 6.5 + 0.5


class Suite(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def cost_cloth(self):
        """вычисляет расход ткани на костюм"""
        return self.height * 2 + 0.3


if __name__ == "__main__":
    mom_coat = Coat("Мамино пальто", 46)
    dad_suite = Suite("Папин костюм", 56)
    son_suite = Suite("Костюм сына", 32)
    total_cost_cloth = mom_coat.cost_cloth + dad_suite.cost_cloth + \
                       son_suite.cost_cloth
    print(f'Расход ткани на семью составил: {total_cost_cloth:.2f}, из них:',
          f'- {mom_coat.name}: {mom_coat.cost_cloth:.2f}',
          f'- {dad_suite.name}: {dad_suite.cost_cloth:.2f}',
          f'- {son_suite.name}: {son_suite.cost_cloth:.2f}', sep='\n')
