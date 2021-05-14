"""Урок 3. Знакомство с Python
5. Реализовать функцию get_jokes() , возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]"""

import random as rnd

# константы кол-ва шуток для тестов
TEST_CNT3, TEST_CNT5, TEST_CNT7 = 3, 5, 7
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
words_for_jokes = nouns, adverbs, adjectives
tests_cnt = TEST_CNT3, TEST_CNT5, TEST_CNT7


def get_jokes(cnt_jokes, *args, repeat_words=False):
    """Возвращает список из count строк-шуток, сформированных из случайных слов,
    взятых из переданных в виде параметров списков (*args) с исходными словами.
    repeat_words - возможность повтора слов в шутках из переданных списков."""

    # print(f"*args=", sep="\n")
    jokes = []
    # если повторов слов в шутках быть не должно repeat_words=False
    if not repeat_words:
        # перемешиваем все переданные на вход списки со словами для шуток
        for item in args:
            rnd.shuffle(item)
        # print("*args shuffle: ", *args, sep="\n")
        for arg in zip(*args):
            # print(type(arg), arg)
            # если уже набрали cnt_jokes шуток, то заканчиваем генерить их
            if len(jokes) == cnt_jokes:
                break
            # если шуток еще недостаточно, то докидываем еще
            jokes.append(" ".join(arg))
        return jokes
    # если повторы слов в шутках допустимы repeat_words=True
    else:
        raw_jokes = []
        # генерим для каждого из переданного списка слов требуемое (cnt_jokes)
        # кол-во случайных слов (повторы возможны)
        for arg in args:
            raw_jokes.append(rnd.choices(arg, k=cnt_jokes))
        # print(raw_jokes)
        # print(*zip(*raw_jokes))
        # склеиваем из сгенерированных наборов строки с шутками в список
        for _ in zip(*raw_jokes):
            # print(_)
            jokes.append(" ".join(_))
        return jokes


# блок тестирования
for test_cnt in tests_cnt:
    print(f"\n{test_cnt} шуток/ки (попытка) без повторов слов:\n",
          get_jokes(test_cnt, *words_for_jokes, repeat_words=False))
    print(f"\n{test_cnt} шуток/ки с повторами слов:\n",
          get_jokes(test_cnt, *words_for_jokes, repeat_words=True))
