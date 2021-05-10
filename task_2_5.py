"""Урок 2. Знакомство с Python
5. Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[ 57.8 , 46.51 , 97 , ...]
A. Вывести на экран эти цены через запятую в одну строку, цена должна
отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если,
например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
B. Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих
товаров по возрастанию, написав минимум кода?"""

price_list = [57.8, 46.01, 2.99, 101.1, 099.99, 1023.11, 666, 777.77, 987.65,
              88.01, 0.01, .99, 13.]
print(f"\nИсходный прайс-лист с ценами на товары (id: {id(price_list)}):\n"
      f"{price_list}")

print("\n5.A. Цены из прайс-листа в строку:")
for item in price_list:
    print("{0:d} руб {1:02.0f} коп,".
          format(int(item), int(round(item - int(item), 2) * 100)), end=' ')

price_list.sort()
print(f"\n\n5.B. Отсортированный по возрастанию прайс-лист с ценами "
      f"(id: {id(price_list)} - Тот же!):\n{price_list}\nВ строку:")
for item in price_list:
    print("{0:d} руб {1:02.0f} коп,".
          format(int(item), int(round(item - int(item), 2) * 100)), end=' ')

copy_price_list = price_list[::-1]
print(f"\n\n5.C. Новый прайс-лист, отсортированный по убыванию цен "
      f"(id: {id(copy_price_list)} - Другой!):\n{copy_price_list}\n")

print("5.D. ТОП-5 самых дорогих товаров из прайс-листа:")
for num, item in enumerate(copy_price_list[:5], 1):
    print("{0:01d}. {1:d} руб {2:02.0f} коп".
          format(num, int(item), int(round(item - int(item), 2) * 100)))
