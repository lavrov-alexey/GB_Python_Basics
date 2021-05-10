"""Урок 1. Знакомство с Python
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28
– делится нацело на 7.
Внимание: использовать только арифметические операции!
b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из
этого списка, сумма цифр которых делится нацело на 7.
c. *Решить задачу под пунктом b не создавая новый список!"""

MAX_COUNT = 1000
DIVISOR = 7

# генерируем список кубов нечетных чисел
cubs_nums = []
for num in range(1, MAX_COUNT + 1, 2):
    cubs_nums.append(num ** 3)

# заводим переменные для накопления искомых сумм по задачам a и b
sum_digit_div, sum_nums_17 = 0, 0
# перебираем все числа из списка кубов нечетных чисел
for num in cubs_nums:
    # для каждого нового числа обнуляем сумму его цифр
    sum_digit_of_num, temp_num = 0, num
    # для задачи b - к каждому числу из списка кубов нечетных добавляем 17
    sum_digit_of_num_17, temp_num_17 = 0, num + 17

    """temp_num_17 всегда больше, поэтому строим цикл по нему
    в цикле отбираем по 1 младшему разряду чисел (по задачам a и b)
    и плюсуем к сумме его цифр, пока целая часть не станет 0 (False)"""
    while temp_num_17:
        # print(f"{temp_num=}, {sum_digit_of_num=}")
        # print(f"{temp_num_17=}, {sum_digit_of_num_17=}")
        sum_digit_of_num += temp_num % 10
        temp_num = temp_num // 10
        sum_digit_of_num_17 += temp_num_17 % 10
        temp_num_17 = temp_num_17 // 10
    # на выходе из while - имеем суммы цифр текущего числа из списка
    # кубов нечетных и текущего + 17
    # если суммы цифр делятся на DIVISOR без остатка - добавляем его к сумме
    if sum_digit_of_num % DIVISOR == 0:
        sum_digit_div += num
    if sum_digit_of_num_17 % DIVISOR == 0:
        sum_nums_17 += num + 17

print("\nСумма чисел ряда из кубов нечетных чисел от 1 до 1000, сумма цифр",
      f"\nкоторых делится нацело на {DIVISOR}: {sum_digit_div:,d}")
print("\nСумма чисел ряда из кубов нечетных чисел (плюс 17 к каждому)\n",
      "от 1 до 1000, сумма цифр которых делится нацело на "
      f"{DIVISOR}: {sum_nums_17:,d}")
