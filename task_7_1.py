"""Урок 7. Знакомство с Python
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей
структурой папок:
|--my_project
    |--settings
    |--mainapp
    |--adminapp
    |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске
(как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем
можно было менять имена папок под конкретный проект; можно ли будет при этом
расширять конфигурацию и хранить данные о вложенных папках и файлах
(добавлять детали)?"""

import os

# храним стартовую структуру папок в dict() (для данной задачи), при
# необходимости расширения - можно вынести в отдельный cfg-файл
PRJ_THREE = {
    'my_project': {
        'settings': None,
        'mainapp': None,
        'adminapp': None,
        'authapp': None}
}


def starter_prj(dir_three: dict, start_path='.'):
    """Рекурентно создает структуру папок в соответствии с переданным словарем
    и путем (по-умолчанию - папка с файлом скрипта)"""

    for dir_name, dir_child in dir_three.items():
        # формируем полный путь папки и проверяем наличие папки
        dir_path = os.path.join(start_path, dir_name)
        dir_exist = os.path.exists(dir_path)
        # папка уже есть и вложенных папок для нее нет - берем след. папку
        if dir_exist and dir_child is None:
            continue
        # папка есть и есть вложенные - переходим к созданию вложенных
        elif dir_exist and dir_child is not None:
            starter_prj(dir_child, start_path=dir_path)
        # папки нет и вложенных папок нет - просто создаем папку
        elif not dir_exist and dir_child is None:
            os.mkdir(dir_path)
        # папки нет, вложенные есть - создаем папку и переходим к вложенным
        else:
            os.mkdir(dir_path)
            starter_prj(dir_child, start_path=dir_path)


if __name__ == '__main__':
    starter_prj(PRJ_THREE)
