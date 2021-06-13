"""Урок 10. Объектно-ориентированное программирование. Продвинутый уровень
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
 (метод __init__()), который должен принимать данные (список списков) для
 формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в
виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и пр."""


class Matrix:
    """реализует сложение и печать 2-мерных числовых матриц """

    def __init__(self, list_of_lists):
        self.matrix = [[col for col in row] for row in list_of_lists]

    def __str__(self):
        SEP_EL = '  '   # разделитель столбцов матрицы при выводе
        END_ROW = '\n'  # завершение строк матрицы при выводе

        # ищем длинну самого длинного числа в матрице для красивого вывода
        max_len_num = 0
        for row in self.matrix:
            for num in row:
                if len(str(num)) > max_len_num:
                    max_len_num = len(str(num))

        # собираем строку матрицы с форматированием
        res_str = ''
        for row in self.matrix:
            row_str = ''
            for num in row:
                # поэлементно добавляем к строке матрицы с разделителем,
                # исходя из длины самого длинного числа в матрице
                row_str += f'{num:{max_len_num}d}{SEP_EL}'
            else:
                # после сборки строки - добавляем заверш. последовательность
                # и готовую строку добавляем к итоговой строке матрицы
                row_str += END_ROW
                res_str += row_str
        return res_str

    def __add__(self, other):
        res_matrix = []
        for row1, row2 in zip(self.matrix, other.matrix):
            res_row_matrix = []
            for num1, num2 in zip(row1, row2):
                res_row_matrix.append(num1 + num2)
            else:
                res_matrix.append(res_row_matrix)
        return Matrix(res_matrix)


if __name__ == '__main__':
    test1 = [
        [111, 12, 13],
        [21, 2245, 23],
        [31, 32, -12345]
        ]
    test2 = [
        [101, 1025, 103],
        [201054, 202, -203],
        [301, 302, 7654321]
    ]

    matrix1 = Matrix(test1)
    matrix2 = Matrix(test2)
    print(f'Матрица 1 (тип: {type(matrix1)}):', matrix1, sep='\n')
    print(f'Матрица 2 (тип: {type(matrix2)}):', matrix2, sep='\n')
    sum_matrix = matrix1 + matrix2
    print(f'Результат сложения 2х матриц (тип: {type(sum_matrix)}):',
          sum_matrix, sep='\n')
