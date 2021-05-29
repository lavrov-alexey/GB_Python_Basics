"""Урок 6. Знакомство с Python
1. Не используя библиотеки для парсинга, распарсить (получить определённые
данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/
nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_adr>, <request_type>,
<requested_resource>). Например:
[...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...]"""

import requests

# шаблоны для парсинга
PAT_ADR = ' - - '
PAT_TYPE = '] "'
PAT_RES = ' /'
LOCAL_LOG_PATH = "nginx_logs.txt"
NET_LOG_PATH = 'https://raw.githubusercontent.com/elastic/examples/master/' \
               'Common%20Data%20Formats/nginx_logs/nginx_logs'


def parser_log_line(log_line):
    """Парсит переданную строку лога вида 'nginx_logs' и возвращает кортеж вида:
    <remote_adr>, <request_type>, <requested_resource>"""

    _tmp = log_line.split(PAT_ADR)
    remote_adr, other = _tmp[0], _tmp[1]
    _tmp = other.split(PAT_TYPE)
    request_type, other = _tmp[1].split(PAT_RES)[0], _tmp[1].split(PAT_RES)[1]
    requested_resource = other.split()[0]
    # выдаем распарсенные в строке параметры в tuple()
    return remote_adr, request_type, requested_resource


if __name__ == '__main__':

    # вариант работы с локальным лог-файлом
    # считываем весь файл сразу, объем позволяет и сразу освобождаем файл
    # with open(LOCAL_LOG_PATH, "r", encoding="utf-8") as f:
    #     log_lines = f.readlines()

    # вариант работы с лог-файлом из сети
    log_lines = requests.get(NET_LOG_PATH).text.splitlines()

    # для каждой строки лога вызываем функцию-парсер и полученные кортежи
    # собираем по ТЗ в список
    res_parsing = [parser_log_line(line) for line in log_lines]
    print(f"Кол-во проанализированных строк лога: {len(res_parsing)}")
    print("Последние 5 эл-тов распарсенного лога:", *res_parsing[-5:], sep='\n')
