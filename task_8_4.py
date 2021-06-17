"""Урок 8. Знакомство с Python
4. Написать декоратор с аргументом-функцией (callback), позволяющий
валидировать входные значения функции и выбрасывать исключение ValueError,
если что-то не так, например:
def val_checker ...
...
@ val_checker (lambda x: x > 0 )
def calc_cube (x):
return x ** 3
>> a = calc_cube(5)
125
>> a = calc_cube(-5)
Traceback (most recent call last):
...
raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?"""

from functools import wraps


def val_checker(func_val):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not func_val(*args):
                raise ValueError(f'Некорректное значение аргументов:', *args)
            return func(*args, **kwargs)

        return wrapper
    return _val_checker


def is_valid_args(*args: int, begin=1, end=10):
    """если *args лежат в диапазоне [begin, end] => True, иначе => False"""
    for arg in args:
        if not (begin <= arg <= end):
            return False
    return True


@val_checker(is_valid_args)
def calc_grade(num=5, grade=3):
    """возводит num в степень grade"""
    return num ** grade


if __name__ == '__main__':
    # тесты
    tests = ((5, 3), (2, 8), (10, 2))
    for _num, _grade in tests:
        print(f'{_num} в степени {_grade} равно {calc_grade(_num, _grade)}')
