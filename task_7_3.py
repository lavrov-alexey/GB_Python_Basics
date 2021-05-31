"""Урок 7. Знакомство с Python
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи
скрипта или «руками» в проводнике).

|--my_project
    |--settings
    |   |--__init__.py
    |   |--dev.py
    |   |--prod.py
    |--mainapp
    |   |--__init__.py
    |   |--models.py
    |   |--views.py
    |   |--templates
    |       |--mainapp
    |           |--base.html
    |           |--index.html
    |--authapp
    |   |--__init__.py
    |   |--models.py
    |   |--views.py
    |   |--templates
    |   |--authapp
    |       |--base.html
    |       |--index.html

Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
    ...
    |--templates
    |   |--mainapp
    |   |   |--base.html
    |   |   |--index.html
    |   |--authapp
    |   |--base.html
    |   |--index.html
"""

import os
import yaml
from pprint import pprint
import shutil

CONFIG_YAML = 'config.yaml'
DIR_TEMPLATES = 'templates'


def get_starter_cfg(path_cfg_file: str):
    """Читает cfg-файл (yaml) и возвращает dict со структурой папок и файлов"""
    with open(path_cfg_file, 'r', encoding='utf-8') as f_cfg:
        return yaml.safe_load(f_cfg)


def starter_project(dir_three: dict, start_path='.'):
    """Создает вложенную структуру папок и файлов по переданному dict и пути"""

    for el_name, el_child in dir_three.items():
        # формируем полный путь элемента
        el_path = os.path.join(start_path, el_name)

        # Для обработки заводим 3 лог. переменных:
        # 1. есть ли уже элемент в файл. системе
        # 2. является ли элемент файлом
        # 3. является ли папка пустой или есть вложенная структура
        el_exist = os.path.exists(el_path)
        el_is_file = True if el_child == 'file' else False
        el_dir_empty = True if el_child is None \
                               and el_child != 'file' else False

        # эл-т уже есть и это или файл или пустая папка => идем дальше
        if (el_exist and el_is_file) or \
                (el_exist and not el_is_file and el_dir_empty):
            continue
        # эл-та нет и это файл => создаем файл и идем дальше
        elif not el_exist and el_is_file:
            with open(el_path, 'w', encoding='utf-8') as ff:
                ff.write('')
        # эл-та нет и он - пустая папка => создаем папку и идем дальше
        elif not el_exist and not el_is_file and el_dir_empty:
            os.mkdir(el_path)
        # эл-т есть - это непустая папка => рекурс. вызов для влож. структуры
        elif el_exist and not el_is_file and not el_dir_empty:
            starter_project(el_child, start_path=el_path)
        # эл-та нет и это непустая папка => создаем папку
        # и для нее делаем рекурс. вызов для влож. структуры
        elif not (el_exist or el_is_file or el_dir_empty):
            os.mkdir(el_path)
            starter_project(el_child, start_path=el_path)


def collect_dirs(src_path, dst_path, dir_name=DIR_TEMPLATES):
    """Создает src_path и копирует туда все вложенные папки dir_name"""

    # находим все папки dir_name, внутри src_path
    dirs_for_copy = [os.path.join(dir_path, dir_name)
                     for dir_path, dirs, files in os.walk(src_path)
                     if dir_name in dirs]

    # создаем/пересоздаем (чистим) папку для сбора шаблонов
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)
    os.mkdir(dst_path)

    # копируем все найденные шаблоны
    for _dir in dirs_for_copy:
        for sub_dir in os.listdir(_dir):
            shutil.copytree(os.path.join(_dir, sub_dir),
                            os.path.join(dst_path, sub_dir))


if __name__ == '__main__':
    starter_structure = get_starter_cfg(CONFIG_YAML)
    pprint(starter_structure)
    starter_project(starter_structure)
    root_project = list(starter_structure.keys())[0]
    template_path = os.path.join(root_project, DIR_TEMPLATES)
    # вызываем функцию сборки папок с шаблонами
    collect_dirs(root_project, template_path, dir_name=DIR_TEMPLATES)
