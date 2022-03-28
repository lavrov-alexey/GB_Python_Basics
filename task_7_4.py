"""Урок 7. Знакомство с Python
4. Написать скрипт, который выводит статистику для заданной папки в виде
словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна
10), а значения — общее количество файлов (в том числе и в подпапках), размер
кот-х не превышает этой границы, но больше предыдущей (начинаем с 0), например:
{100: 15,
1000: 3,
10000: 7,
100000: 2}
Тут 15 файлов размером не более 100 байт;
3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat."""

import os

DEFAULT_DIR = 'some_data'
STAT_BY_SIZE = [100, 1000, 10000, 100000]


def stat_dir(dir_path: str, src_stat: list):
    """Возвращает dict со статистикой по папке dir_path в соотв. с [src_stat]"""
    # формируем список границ размеров файлов для статистики по возрастанию
    src_stat.sort()
    # создаем заготовку словаря для сбора статистики
    stat_dict = {size: 0 for size in src_stat}

    # пробегаемся рекурсивно по текущей папке и подпапкам
    for curr_path_dir, _, __ in os.walk(dir_path):
        # перебираем все файлы в папке и вытягиваем размер каждого
        for item in os.scandir(curr_path_dir):
            if item.is_dir():  # папки нас не интересуют
                continue
            file_size = os.stat(item).st_size
            # для каждого файла последовательно сравниваем с каждой границей
            # по возрастанию размера
            for size_border in src_stat:
                # размер меньше границы - плюсуем кол-во в текущ. границу
                # и берем след. файл, если больше - сравниваем со след. границей
                if file_size < size_border:
                    stat_dict[size_border] += 1
                    break
    return stat_dict


if __name__ == '__main__':
    stat = stat_dir(DEFAULT_DIR, STAT_BY_SIZE)
    # блок вывода
    abs_path = os.path.join(os.getcwd(), DEFAULT_DIR)
    print(f'\nВ папке {abs_path} - всего {sum(stat.values())} файлов,\n'
          f'статистика количества файлов по их размерам(в байтах):\n')
    for size_brdr, count_files in stat.items():
        print(f'{size_brdr}:\t{count_files}')
