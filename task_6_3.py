"""Урок 6. Знакомство с Python
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом —
данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка —
один пользователь, разделитель между значениями — запятая. Написать код,
загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
значения — данные о хобби. Сохранить словарь в файл.
Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
записей, чем в файле с ФИО, задаём в словае значение None. Если наоборот —
выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз
меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи"""

from os.path import exists
import json
from itertools import zip_longest


def create_users_hobby(file_users: str, file_hobby: str):
    """Формирует словарь вида {ФИО: хобби} из поданных на вход файлов
    с ФИО и хобби. Данные из файлов не обрабатываем - пишем как есть!
    Если в файле с хобби, меньше записей - пишем {ФИО: None}.
    Если в файле с ФИО, меньше записей — выход из скрипта с кодом 1"""

    with open(file_users, 'r', encoding='utf-8') as f_users, \
            open(file_hobby, 'r', encoding='utf-8') as f_hobby:
        users = f_users.read().splitlines()
        hobbs = f_hobby.read().splitlines()

        # если ФИО меньше, чем хобби - завершаем скрипт с кодом "1"
        if len(users) < len(hobbs):
            print(f"Кол-во записей в файле {USERS_FILE} не должно быть "
                  f"меньше, чем кол-во записей в файле {HOBBY_FILE}!")
            exit(1)

        # формируем dict через генераторы по количеству хобби
        name_gen = (name for name in users)
        hobby_gen = (hobby for hobby in hobbs)
        return {name: hobby for hobby, name in zip_longest(hobby_gen, name_gen)}


if __name__ == '__main__':

    RESULT_FILE = 'users_hobby.json'
    USERS_FILE = 'users.csv'
    HOBBY_FILE = 'hobby.csv'

    # если вх. файлов нет - ругаемся и выходим с кодом 2
    if not (exists(USERS_FILE) and exists(HOBBY_FILE)):
        print(f"Файл/ы с входными данными ({USERS_FILE} и/или "
              f"{HOBBY_FILE}) - не найден/ы!")
        exit(2)
    users_hobby = create_users_hobby(USERS_FILE, HOBBY_FILE)
    print(f"Тип результата: {type(users_hobby)}\n"
          f"Результат работы скрипта:\n{users_hobby}\n")

    # блок записи в файл (сериализация)
    with open(RESULT_FILE, 'w', encoding="utf-8") as f:
        f.write(json.dumps(users_hobby))

    # блок проверки (десериализация)
    with open(RESULT_FILE, 'r', encoding='utf-8') as f:
        content = json.loads(f.read())
        print(f"Проверка - результат десериализации итогов работы скрипта.\n"
              f"Тип рез-та: {type(content)}.\n"
              f"Рез-т работы скрипта:\n{content}")
