"""Урок 6. Знакомство с Python
6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно
быть два скрипта с интерфейсом командной строки: для записи данных и для вывода
на экран записанных данных. При записи передавать из командной строки значение
суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
● просто запуск скрипта — выводить все записи;
● запуск скрипта с одним параметром-числом — выводить все записи с номера,
равного этому числу, до конца;
● запуск скрипта с двумя числами — выводить записи, начиная с номера, равного
первому числу, по номер, равный второму числу, включительно.

Подумать, как избежать чтения всего файла при реализации второго и третьего
случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей
начинается с 1.

Примеры запуска скриптов:
python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1"""

from sys import argv
import math

DATA_FILE = 'bakery.csv'  # путь к файлу с данными по суммам продаж
SUM_TMPL = '+13.2f'  # шаблон хранения сумм продаж
LINE_OFFSET = 15  # длина 1й записи с суммой продаж (с учетом служ. данных)


def get_sales(start_pos=1, end_pos=None):
    """Возвращает список строк с продажами с номера start_pos по end_pos"""
    with open(DATA_FILE, 'r', encoding='utf-8') as f:

        # обработка вызова с полным выводом
        if start_pos == 1 and end_pos is None:
            return f.read()

        start_offset = LINE_OFFSET * (start_pos - 1)
        f.seek(start_offset)  # прыгаем сразу в стартовую позицию

        target_sales = []  # для сбора запрошенных продаж
        line = f.readline().strip()
        sales_for_show = None if end_pos is None else end_pos - start_pos

        # пока есть записи и при этом нужно читать до конца или не дошли до
        # заданной границы - собираем продажи
        while line and (sales_for_show is None or sales_for_show >= 0):
            target_sales.append(line)
            line = f.readline().strip()
            sales_for_show -= 1
        return target_sales


if __name__ == '__main__':

    # кол-во переданных пар-ров (не считая самого скрипта)
    cnt_pars = len(argv) - 1

    # вызов без параметров (все записи)
    if cnt_pars == 0:
        print(get_sales())

    # вызов с 1 параметром (старт)
    elif cnt_pars == 1 and argv[1].isdigit() and int(argv[1]) > 0:
        print(*get_sales(start_pos=int(argv[1])), sep='')
    # вызов скрипта с 2 параметрами (старт-стоп)
    elif cnt_pars == 2 and argv[1].isdigit() and argv[2].isdigit()\
            and 0 < int(argv[1]) <= int(argv[2]):
        print(*get_sales(start_pos=int(argv[1]), end_pos=int(argv[2])),
              sep='\n')
    else:
        print('Ожидается передача не более 2х параметров-чисел,\n'
              '1 параметр - start > 0, 2 параметр - end (start <= end)!')
        exit(1)
