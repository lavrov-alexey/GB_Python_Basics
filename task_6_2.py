"""Урок 6. Знакомство с Python
1. (решение - task_6_1.py) Не используя библиотеки для парсинга, распарсить
(получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/
nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_adr>, <request_type>,
<requested_resource>). Например:
[...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...]
2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов
по данным файла логов из задания 1.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен
работать даже с файлами, размер которых превышает объем ОЗУ компьютера."""

if __name__ == '__main__':

    PAT_ADR = ' - - '  # шаблон для парсинга адреса в логах вида nginx_logs.txt
    LOG_PATH = "nginx_logs.txt"  # файл логов web-сервера для анализа

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        stats_adr = dict()  # для накопления статистики вида {adr: cnt_req}
        # по ТЗ - не читаем файл целиком, а построчно пробегаемся по файлу и
        # собираем статистику по адресам
        for line in f:
            adr = line.split(PAT_ADR)[0]  # вычленяем из строки лога адрес
            # увелич. счетчик (если адрес уже был), либо заводим его в словарь
            if adr in stats_adr.keys():
                stats_adr[adr] += 1
            else:
                stats_adr[adr] = 1
    total_req = sum(stats_adr.values())  # общее кол-во запросов в логе
    # сортируем словарь со стат. по кол-ву запросов и берем данные "спаммера"
    spam_adr, spam_cnt = sorted(stats_adr.items(), key=lambda x: x[1])[-1]

    print(f"Всего запросов в лог-файле '{LOG_PATH}': {total_req}")
    print(f"С адреса {spam_adr} ('спаммер'), зафиксировано {spam_cnt} запросов "
          f"({(spam_cnt / total_req) * 100:.2f} %)")
