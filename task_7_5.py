"""Урок 7. Знакомство с Python
4. Написать скрипт, который выводит статистику для заданной папки в виде
словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна
10), а значения — общее количество файлов (в том числе и в подпапках), размер
которых не превышает этой границы, но больше предыдущей (начинаем с 0),например:
{100: 15,
1000: 3,
10000: 7,
100000: 2}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100
и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat."""
"""
5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки 
в виде словаря, в котором ключи те же, а значения — кортежи вида 
(<files_quantity>, [<files_extensions_list>]), например:
{
100: (15, ['txt']),
1000: (3, ['py', 'txt']),
10000: (7, ['html', 'css']),
100000: (2, ['png', 'jpg'])
}
Сохраните результаты в файл <folder_name>_summary.json в той же папке, 
где запустили скрипт."""

import os

DEFAULT_DIR = 'some_data'
STAT_BY_SIZE = [100, 1000, 10000, 100000]


def stat_dir_ext(dir_path: str, src_stat: list):
    """Возвращает dict() со статистикой по рамерам [src_stat] и расширениям
    файлов папки dir_path"""
    # формируем список границ размеров файлов для статистики по возрастанию
    src_stat.sort()
    # создаем заготовку словаря для сбора статистики
    stat_dict = {size: [0, []] for size in src_stat}

    # пробегаемся рекурсивно по текущей папке и подпапкам
    for curr_path_dir, _, __ in os.walk(dir_path):
        # перебираем все файлы в папке и вытягиваем размер и расширение каждого
        for item in os.scandir(curr_path_dir):
            if item.is_dir():  # папки нас не интересуют
                continue
            file_size = os.stat(item).st_size
            file_ext = item.name.rsplit('.', 1)[-1]
            # для каждого файла последовательно сравниваем с каждой границей
            # по возрастанию размера
            for size_border in src_stat:
                # размер меньше границы - плюсуем кол-во в текущ. границу
                # и берем след. файл, если больше - сравниваем со след. границей
                if file_size < size_border:
                    stat_dict[size_border][0] += 1
                    if file_ext not in stat_dict[size_border][1]:
                        stat_dict[size_border][1].append(file_ext)
                    break
    return stat_dict


if __name__ == '__main__':

    stats = stat_dir_ext(DEFAULT_DIR, STAT_BY_SIZE)

    # блок вывода
    abs_path = os.path.join(os.getcwd(), DEFAULT_DIR)
    cnt_of_files = sum(cnt[0] for cnt in stats.values())
    print(f'\nВ папке {abs_path} - всего {cnt_of_files} файлов,\n'
          f'статистика количества файлов по их размерам(в байтах):\n')
    for size_brdr, count_files in stats.items():
        print(f'{size_brdr}:\t{count_files}')
