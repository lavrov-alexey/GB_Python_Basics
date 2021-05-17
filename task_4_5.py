"""Урок 4. Знакомство с Python
5. *(вместо 4) Доработать скрипт из предыдущего задания:
теперь он должен работать и из консоли.
Например:
python task_4_5.py USD
75.18, 2020-09-05"""

import sys
import utils
# import requests
# from decimal import Decimal
# from datetime import datetime

if __name__ == '__main__':
    # коды валют для тестов
    TEST_CODE_CURRENCY = "USD", "EUR", "FFF", "usd", "eUr"

    # Блок CLI. При вызове из командной строки и передаче любого кол-ва кодов валют -
    # в консоль будут выведены их курсы, например:
    # >python task_4_5.py USD EUR gBp
    # На 2021-03-12 курс USD: 73.4996 руб.
    # На 2021-03-12 курс EUR: 87.7585 руб.
    # На 2021-03-12 курс gBp: 102.5099 руб.
    codes_currs = sys.argv[1:]
    for code_curr in codes_currs:
        my_rate, my_date = utils.currency_rates(code_curr)
        if my_rate:  # если курс есть (не None)
            print(f"На {my_date.strftime('%A, %d.%m.%Y')} "
                  f"курс {code_curr}: {my_rate} руб.")
        else:
            print(rf"Код валюты {code_curr}: отсутствует в источнике. ¯\_(:))_/¯")

    # блок вывода без CLI
    # print("\nВ качестве источника курсов валют используется ресурс: "
    #       "http://www.cbr.ru/scripts/XML_daily.asp\n")
    # for code_curr in TEST_CODE_CURRENCY:
    #     my_rate, my_date = utils.currency_rates(code_curr)
    #     if my_rate:  # если курс есть (не None)
    #         print(f"На {my_date.strftime('%A, %d.%m.%Y')} "
    #               f"курс {code_curr}: {my_rate} руб.")
    #     else:
    #         print(rf"Код валюты {code_curr}: отсутствует в источнике. ¯\_(ツ)_/¯")
