"""Урок 8. Знакомство с Python 1. Написать функцию email_parse(<email_address>),
которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError. Пример:

>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}

>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>" , line 1 , in <module>
...
raise ValueError(msg) ValueError: wrong email: someone@geekbrainsru

Примечание:
подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile() ?
"""

import re

TEST_EMAIL = ["someone@geekbrains.ru",
              'someone@geekbrainsru',
              '7242636@mail.ru d42',
              'rusak-8+8@mail.ru',
              "de'w@w.w",
              "°@.ph', ",
              "'_`@_post.gi",
              '7242636@mail.ru']
TEMPLATE_EMAIL = r"\b(?P<username>[\w\d.'_+-]+)@" \
                 r"(?P<domain>(?:[\w\d_-]+\.)+\w{2,3})$"


def email_parse(email_address: str, tmpl_email):
    """Возвращает dict(username: someone, domain: something) из переданного
    email_address Например: 'someone@geekbrains.ru' =>
    {'username': 'someone', 'domain': 'geekbrains.ru'}"""

    result = tmpl_email.search(email_address)
    if result:
        return result.groupdict()
    raise ValueError(f'\nWrong e-mail: {email_address}\n')


if __name__ == '__main__':
    cmp_template_email = re.compile(TEMPLATE_EMAIL)
    for email in TEST_EMAIL:

        try:
            res_pars = email_parse(email, cmp_template_email)
        except ValueError:
            print(f"{email} - АДРЕС НЕ ВАЛИДЕН!\n"
                  f"Поймано исключение ValueError!\n")

        user, domain = res_pars.values()
        print(f"{email} - адрес валиден!\n"
              f"Имя пользователя: {user}, домен: {domain}\n")
