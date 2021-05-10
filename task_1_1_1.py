"""Урок 1. Знакомство с Python
1. Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d(*). в остальных случаях: <d> дн <h> час <m> мин <s> сек.

Вариант 1 - реализация без цикла"""

# заводим константы для пересчета интервалов
SEK_IN_MIN, MIN_IN_HOUR, HOUR_IN_DAY = 60, 60, 24
# берем усредненное кол-во дней в мес., с учетом високосного года
DAY_IN_MONTH, MONTH_IN_YEAR = (3 * 365 / 12 + 366 / 12) / 4, 12

# получаем с консоли целое число (исключения не ловим)
dur_in_sek = int(input('Введите интервал времени в секундах (целое положительное'
                       ' число) для конвертации: '))

# последовательно переводим интервалы в минуты, часы, дни
dur_min, dur_sek = dur_in_sek // SEK_IN_MIN, dur_in_sek % SEK_IN_MIN
dur_hour, dur_min = dur_min // MIN_IN_HOUR, dur_min % MIN_IN_HOUR
dur_day, dur_hour = dur_hour // HOUR_IN_DAY, dur_hour % HOUR_IN_DAY
# по ТЗ не детализировалось, поэтому длительность месяца в днях берем
# усредненно с учетом високосного года, с округлением результата
dur_month, dur_day = round(dur_day // DAY_IN_MONTH), round(dur_day % DAY_IN_MONTH)
dur_year, dur_month = dur_month // MONTH_IN_YEAR, dur_month % MONTH_IN_YEAR

# вывод инфы - выводим по ТЗ, начиная с ненулевого старшего периода
if dur_year > 0:
    print(f"\n{dur_year} лет {dur_month} мес {dur_day} дн {dur_hour} час "
          f"{dur_min} мин {dur_sek} сек")
elif dur_month > 0:
    print(f"\n{dur_month} мес {dur_day} дн {dur_hour} час {dur_min} мин "
          f"{dur_sek} сек")
elif dur_day > 0:
    print(f"\n{dur_day} дн {dur_hour} час {dur_min} мин {dur_sek} сек")
elif dur_hour > 0:
    print(f"\n{dur_hour} час {dur_min} мин {dur_sek} сек")
elif dur_min > 0:
    print(f"\n{dur_min} мин {dur_sek} сек")
else:
    print(f"\n{dur_sek} сек")

print("\n* Для расчета кол-ва месяцев - берем усредненное значение дней в месяце\n"
      "с учетом високосных лет (3 * 365 / 12 + 366 / 12) / 4 = "
      f"{(3 * 365 / 12 + 366 / 12) / 4} дней")
