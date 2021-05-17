"""Урок 4. Знакомство с Python
2. Написать функцию currency_rates(), принимающую в качестве аргумента код
валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по
отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно
запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя
только методы класса str, решить поставленную задачу? Функция должна возвращать
результат числового типа, например float. Подумайте: есть ли смысл для работы с
денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется
код функции при этом? Если в качестве аргумента передали код валюты, которого нет
в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
в каком регистре был передан аргумент? В качестве примера выведите курсы
доллара и евро."""

import requests
from decimal import Decimal


def currency_rates(code_currency: str):
    """ Returns actual currency rate in RUR for his code (eg "USD") from source:
        http://www.cbr.ru/scripts/XML_daily.asp
        If code currency is not find => None"""

    # делаем нечувствительность к регистру кода валюты
    code_currency = code_currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    # проверяем - есть ли переданный код валюты в ответе ресурса (нет => None)
    if response.text.find(code_currency) == -1:
        return  # => None
    # последовательно вычленяем собственно значение курса запрошенной валюты
    current_rate = response.text.split(f"<CharCode>{code_currency}</CharCode>")
    current_rate = current_rate[1].split('<Value>')
    current_rate = current_rate[1].split('</Value>')[0]
    # для перевода в числовой тип меняем разделитель дробной части
    current_rate = current_rate.replace(",", ".")
    return Decimal(current_rate)


if __name__ == "__main__":
    # коды валют для тестов
    TEST_CODE_CURRENCY = "USD", "EUR", "FFF", "usd", "eUr"

    # блок вывода
    print("\nВ качестве источника курсов валют используется ресурс:\n"
          "http://www.cbr.ru/scripts/XML_daily.asp\n")
    for code_curr in TEST_CODE_CURRENCY:
        rate_curr = currency_rates(code_curr)
        if rate_curr:  # если курс есть (не None)
            print(f"Курс {code_curr}: {rate_curr} руб.")
        else:
            print(rf"Код валюты {code_curr}: отсутствует в источнике. ¯\_(ツ)_/¯")