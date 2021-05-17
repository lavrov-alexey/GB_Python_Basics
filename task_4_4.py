"""Урок 4. Знакомство с Python
4. Написать свой модуль utils и перенести в него функцию currency_rates() из
предыдущего задания. Создать скрипт, в котором импортировать этот модуль и
выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит."""

import utils

if __name__ == "__main__":
    # коды валют для тестов
    TEST_CODE_CURRENCY = "BYN", "gbP", "XXX"

    # блок вывода
    print("\nРезультат работы функции currency_rates из своего модуля utils.py:\n")
    print("В качестве источника курсов валют используется ресурс: "
          "http://www.cbr.ru/scripts/XML_daily.asp\n")
    for code_curr in TEST_CODE_CURRENCY:
        my_rate, my_date = utils.currency_rates(code_curr)
        if my_rate:  # если курс есть (не None)
            print(f"На {my_date.strftime('%A, %d.%m.%Y')} "
                  f"курс {code_curr}: {my_rate} руб.")
        else:
            print(rf"Код валюты {code_curr}: отсутствует в источнике. ¯\_(ツ)_/¯")
    print("\n********** Ничего постороннего из модуля utils.py не выводится "
          "**********")
