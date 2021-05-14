"""Урок 3. Знакомство с Python
2. *(вместо задачи 1)
Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
с числительными, начинающимися с заглавной буквы — результат тоже должен быть
с заглавной. Например:
# num_translate_adv("One")  # 'Один'
# num_translate_adv("two")  # 'два'"""

DICT_TRANSLATE = {'zero': 'ноль',
                  'one': 'один',
                  'two': 'два',
                  'three': 'три',
                  'four': 'четыре',
                  'five': 'пять',
                  'six': 'шесть',
                  'seven': 'семь',
                  'eight': 'восемь',
                  'nine': 'девять',
                  'ten': 'десять'}

test_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine', 'ten', 'something', 'One', 'TWo',
             'THREE', 'fOur', 'Something']


def num_translate_adv(numeral, dictionary=DICT_TRANSLATE):
    """Translating by dictionary eng-numeric (0-10) to rus, if not exist => None"""
    if numeral.istitle():
        return str(dictionary.get(numeral.lower())).title()
    return dictionary.get(numeral)


print(*(f'"{num}" => "{num_translate_adv(num)}"' for num in test_list), sep='\n')
