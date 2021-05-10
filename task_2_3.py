"""Урок 2. Знакомство с Python
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5',
'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём
до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха',
'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
3. *(вместо задачи 2) Решить задачу 2 не создавая новый список (in place)
Эта задача намного серьёзнее, чем может сначала показаться."""

in_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']
print(f"\nОригинальный список (id: {id(in_list)}):\n{in_list}")
idx = 0
while idx < len(in_list):
    is_int, sign, word = False, '', in_list[idx]
    """Если 'слово' состоит из цифр или начинается со знака и дальше цифры,
    то запоминаем знак (если есть), вырезаем его и поднимаем флаг is_int"""
    if word.startswith(('+', '-')) and word[1:].isdigit():
        sign, word, is_int = word[0], word[1:], True
    elif word.isdigit():
        is_int = True

    # если текущее "слово" из списка - целое число
    if is_int:
        current_int = abs(int(word))
        # если число однозначное - дополняем до 2х знаков ведущим 0
        if 0 <= current_int < 10:
            in_list[idx] = "".join((sign, '0', word))
        # дополняем целое число слева и справа в списке кавычками
        in_list.insert(idx, '"')
        in_list.insert(idx + 2, '"')
        idx += 2  # т.к. добавили ", то сдвигаемся в списке на 2 позиции
    else:  # если текущее "слово" из списка не целое число
        idx += 1  # то просто переходим к следующему "слову" из списка

print(f"\nОбработанный список (id: {id(in_list)} - Тот же!):\n{in_list}")

# сборка обработанной строки с подавлением лишних пробелов
result_str, idx = "", 0
while idx < len(in_list):
    if in_list[idx] == '"':
        result_str += in_list[idx] + in_list[idx + 1] + in_list[idx + 2] + " "
        idx += 3
    else:
        result_str += in_list[idx] + " "
        idx += 1

print("\nСтрока из обработанного списка:", result_str.rstrip(), sep='\n')
