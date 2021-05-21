"""Урок 5. Знакомство с Python
5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования
в исходном списке, например:
src_nums = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniq_nums = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации."""

import random
from time import perf_counter

CNT_NUMS_SHOW = 30
# Последовательность из ТЗ
# src_nums = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Случайная последовательность для тестирования алгоритмов
src_nums = [random.randint(0, 2000) for _ in range(10 ** 4)]


def get_uniq_nums(nums):
    """Возвращает list c уникальными числами из переданного на вход списка"""
    # заводим словарь, в котором ключи - числа из входной последовательности,
    # а значения - либо True (если число уникально), либо False (если не уникально)
    # пользуемся тем, что начиная с v.3.7 словари хранят порядок элементов
    uniq_nums = {}
    for num in nums:
        # если числа в ключах нет - пишем в значения True, если уже есть - None
        uniq_nums[num] = False if num in uniq_nums else True
    return [key for key, value in uniq_nums.items() if value]


if __name__ == "__main__":
    print(f"\nПервые {CNT_NUMS_SHOW} элементов исходной последовательности из "
          f"{len(src_nums):,d} случайных эл-тов:\n{src_nums[:CNT_NUMS_SHOW]}\n")
    # решение "в лоб"
    start = perf_counter()
    uniq_nums1 = [num for num in src_nums if src_nums.count(num) == 1]
    print(f"Время выполнения 'в лоб': {perf_counter() - start}")
    print(f"Кол-во найденных уникальных элементов: {len(uniq_nums1)}")
    print(f"Первые {CNT_NUMS_SHOW} уникальных элементов:\n"
          f"{uniq_nums1[:CNT_NUMS_SHOW]}")
    print("******************************************")
    # решение через словарь
    start = perf_counter()
    uniq_nums2 = get_uniq_nums(src_nums)
    print(f"Время выполнения 'через словарь': {perf_counter() - start}")
    print(f"Кол-во найденных уникальных элементов: {len(uniq_nums2)}")
    print(f"Первые {CNT_NUMS_SHOW} уникальных элементов:\n"
          f"{uniq_nums2[:CNT_NUMS_SHOW]}")
