"""Урок 3. Знакомство с Python
1. Написать функцию num_translate(), переводящую числительные от 0 до 10
c английского на русский язык.
Например: num_translate("one")  # "один"
          num_translate("eight")  # "восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше
хранить информацию, необходимую для перевода: какой тип данных выбрать,
в теле функции или снаружи."""

DICT_TRANSLATE = {"zero": "ноль",
                  "one": "один",
                  "two": "два",
                  "three": "три",
                  "four": "четыре",
                  "five": "пять",
                  "six": "шесть",
                  "seven": "семь",
                  "eight": "восемь",
                  "nine": "девять",
                  "ten": "десять"}

test_list = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "something", "One", "TWo",
             "THREE", "fOur", "Something"]


def num_translate(numeral, dictionary=DICT_TRANSLATE):
    """Translating by dictionary eng-numeric (0-10) to rus, if not exist => None"""
    return dictionary.get(numeral)


print(*(f'"{num}" => "{num_translate(num)}"' for num in test_list), sep="\n")
