import requests
from decimal import Decimal
from datetime import datetime


def currency_rates(code_currency):
    """ Returns actual currency rate in RUR for his code (eg "USD") and date of rate
    (in datetime.date format) from source: http://www.cbr.ru/scripts/XML_daily.asp
    If code currency is not find => None"""

    # делаем нечувствительность к регистру переданного кода валюты
    code_currency = code_currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    # проверяем - есть ли переданный код валюты в ответе ресурса (нет => None)
    if response.text.find(code_currency) == -1:
        return None, None  # для совместимости возвращаем тоже tuple

    # вычленяем собственно значение курса запрошенной валюты и дату
    current_rate = response.text.split(f"<CharCode>{code_currency}</CharCode>")
    # отвлекаемся на дату
    date_rate = current_rate[0].split('<ValCurs Date="')
    date_rate = date_rate[1][:10]  # здесь у нас уже есть дата
    # преобразуем дату в формат datetime
    date_rate = datetime.strptime(date_rate, '%d.%m.%Y')
    # занимаемся дальше курсом
    current_rate = current_rate[1].split('<Value>')
    current_rate = current_rate[1].split('</Value>')[0]

    # для перевода курса в числовой тип меняем разделитель дробной части
    current_rate = current_rate.replace(",", ".")
    return Decimal(current_rate), date_rate


# часть, которая не должна выполняться при импорте модуля
if __name__ == '__main__':
    # коды валют для тестов
    TEST_CODE_CURRENCY = "USD", "EUR", "FFF", "usd", "eUr"

    print('\n********* При импорте модуля этого не должно выводиться *********\n')
    print("В качестве источника курсов валют используется ресурс: "
          "http://www.cbr.ru/scripts/XML_daily.asp\n")
    for code_curr in TEST_CODE_CURRENCY:
        my_rate, my_date = currency_rates(code_curr)
        if my_rate:  # если курс есть (не None)
            print(f"На {my_date.strftime('%A, %d.%m.%Y')} "
                  f"курс {code_curr}: {my_rate} руб.")
        else:
            print(rf"Код валюты {code_curr}: отсутствует в источнике. ¯\_(ツ)_/¯")
