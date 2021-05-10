"""Урок 2. Знакомство с Python
1. Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2"""

expr_mult = 15 * 3
expr_div = 15 / 3
expr_div_mod = 15 // 2
expr_degree = 15 ** 2

print(f"Тип результата выражения 15 * 3 = {expr_mult}: {type(expr_mult)}")
print(f"Тип результата выражения 15 / 3 = {expr_div}: {type(expr_div)}")
print(f"Тип результата выражения 15 // 3 = {expr_div_mod}: {type(expr_div_mod)}")
print(f"Тип результата выражения 15 % 3 = {expr_degree}: {type(expr_degree)}")
