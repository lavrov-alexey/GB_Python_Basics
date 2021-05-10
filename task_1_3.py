"""Урок 1. Знакомство с Python
3. Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов», задаем число 2
— получаем «2 процента».
Вывести все склонения для проверки."""

MAX_NUMBER = 20
DECLINATIONS = ("процент", "процента", "процентов")

for percent in range(MAX_NUMBER + 1):
    if percent == 1:
        print(percent, DECLINATIONS[0])
    elif 1 < percent < 5:
        print(percent, DECLINATIONS[1])
    else:
        print(percent, DECLINATIONS[2])

# Факультатив - склонение любого введенного положительного числа
number = int(input("\nВведите положительное целое число для склонения %: "))
if number % 10 == 1 and number % 100 != 11:
    print(number, DECLINATIONS[0])
elif 1 < number % 10 < 5 and not (11 < number % 100 < 20):
    print(number, DECLINATIONS[1])
else:
    print(number, DECLINATIONS[2])
