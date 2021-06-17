"""Урок 8. Знакомство с Python
3. Написать декоратор для логирования типов позиционных аргументов функции,
например:
def type_logger ...
...
@ type_logger
def calc_cube (x):
    return x ** 3
>> a = calc_cube( 5 )
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? Сможете ли решить задачу для
именованных аргументов? Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
>> a = calc_cube(5)
calc_cube(5: <class 'int'>)"""

from functools import wraps


def type_logger(func):

    @wraps(func)
    def arg_wrapper(*args, **kwargs):
        args_log = ", ".join((f'{arg}: {type(arg)}' for arg in args))
        kwargs_log = ", ".join((f'{key}={value} {type(value)}'
                                for key, value in kwargs.items()))
        log_line = f"{func.__name__}({args_log}" \
                   f"{', ' if args and kwargs else ''}{kwargs_log})"
        res_func = func(*args, **kwargs)
        return res_func, log_line

    return arg_wrapper


@type_logger
def calc_grade(num=5, grade=3):

    return num ** grade


if __name__ == '__main__':
    # тесты
    test = calc_grade(5, 3)
    print(*test, sep='\n')
    test = calc_grade(grade=5, num=2)
    print(*test, sep='\n')
    test = calc_grade(10, grade=3)
    print(*test, sep='\n')
    test = calc_grade()
    print(*test, sep='\n')
