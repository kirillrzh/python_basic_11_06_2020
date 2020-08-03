from copy import deepcopy

class Matrix:
    result_matrix = []

    def __init__(self, number_lines=3, number_items_lines=3, auto=False, auto_matrix=[[5, 5], [5, 5], [5, 5]]):
        if auto:
            self.result_matrix = auto_matrix
            return
        for lines in range(0, number_lines):
            line_list = []
            for item in range(0, number_items_lines):
                while True:
                    item_line = input(f'Строка {lines + 1} позиция {item + 1}, введите число - ')
                    if item_line.isdigit():
                        item_line = int(item_line)
                        line_list.append(item_line)
                        break
                    else:
                        print('Принимается только число!')
            self.result_matrix.append(line_list)

    def __str__(self):
        str_matrix_result = ''
        for line in range(0, len(self.result_matrix)):
            str_matrix_result += ' '.join(map(lambda item: str(item), self.result_matrix[line]))
            if line < len(self.result_matrix) - 1:
                str_matrix_result += '\n'
        return str_matrix_result

    def __add__(self, other):


        def add_lines(matrix_list):
            try:
                check_index = matrix_list[lines]
            except IndexError:
                matrix_list.append([])

        def add_item_in_lines(matrix_list):
            try:
                check_index = matrix_list[lines][item]
            except IndexError:
                matrix_list[lines].append(0)

        one_matrix = deepcopy(self.result_matrix)
        two_matrix = deepcopy(other.result_matrix)
        sum_matrix = []

        for lines in range(0, len(one_matrix) if len(one_matrix) >
                                                 len(two_matrix) else len(two_matrix)):
            sum_line_item = []

            add_lines(one_matrix)
            add_lines(two_matrix)

            for item in range(0, len(one_matrix[lines]) if len(one_matrix[lines]) >
                                                           len(two_matrix[lines]) else len(two_matrix[lines])):
                add_item_in_lines(one_matrix)
                add_item_in_lines(two_matrix)
                sum_item = one_matrix[lines][item] + two_matrix[lines][item]
                sum_line_item.append(sum_item)
            while True:
                try:
                    if len(sum_line_item) == len(sum_matrix[0]):
                        break
                    else:
                        sum_line_item.append(0)
                        if len(one_matrix[lines]) < len(sum_line_item):
                            one_matrix[lines].append(0)
                        if len(two_matrix[lines]) < len(sum_line_item):
                            two_matrix[lines].append(0)
                except IndexError:
                    break

            sum_matrix.append(sum_line_item)
        return sum_matrix


matrix_1 = Matrix(auto=True, auto_matrix=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
print(matrix_1)
print('+')

matrix_2 = Matrix(auto=True, auto_matrix=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(matrix_2)
print('=')

print(matrix_1 + matrix_2)

matrix_3 = matrix_1 + matrix_2

result_sum_matrix = Matrix(auto=True, auto_matrix=matrix_3)
print('А если красиво то:')
print(result_sum_matrix)