"""Урок 5. Знакомство с Python
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое
слово yield , например:
#odd_to_15 = odd_nums(15)
#next(odd_to_15)
1
#next(odd_to_15)
3
...
#next(odd_to_15)
15
#next(odd_to_15)
...StopIteration..."""


def odd_nums_gen(max_odd_num):
    for odd_num in range(1, max_odd_num + 1, 2):
        yield odd_num


if __name__ == "__main__":
    odd_to_15 = odd_nums_gen(15)
    print("1 значение генератора нечетных чисел:", next(odd_to_15))
    print("2 значение генератора нечетных чисел:", next(odd_to_15))
    print("Остальные значения генератора нечетных чисел:", *odd_to_15)
    print("Попытка взять след. значение из истощенного генератора", next(odd_to_15))
