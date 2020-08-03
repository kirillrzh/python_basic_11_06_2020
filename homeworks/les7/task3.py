import math


class OrganismCell:

    def __init__(self, quantity_cell=0):
        self.quantity_cell = quantity_cell

    def __add__(self, other):
        sum_quantity_cell = self.quantity_cell + other.quantity_cell
        print(f'Сумма клеток {self.quantity_cell} и {other.quantity_cell} равна {sum_quantity_cell}')
        return sum_quantity_cell

    def __sub__(self, other):
        sub_quantity_cell = self.quantity_cell - other.quantity_cell
        if sub_quantity_cell == 0:
            print('Клетки поглатили друг друга, теперь количество их равно дырке от бублика!')
        elif sub_quantity_cell < 0:
            print('Разность отрицательна, введены некорректные значения!')
        else:
            print(f'Разность клеток {self.quantity_cell} и {other.quantity_cell} равна {sub_quantity_cell}')
        return sub_quantity_cell

    def __mul__(self, other):
        mul_quantity_cell = self.quantity_cell * other.quantity_cell
        print(f'Произведение клеток {self.quantity_cell} и {other.quantity_cell} равно {mul_quantity_cell}')
        return mul_quantity_cell

    def __truediv__(self, other):
        truediv_quantity_cell = math.floor(self.quantity_cell / other.quantity_cell)
        print(f'Отношение клеток {self.quantity_cell} и {other.quantity_cell} равно {truediv_quantity_cell}')
        return truediv_quantity_cell

    def __str__(self):
        return f'Это организм состоит из {self.quantity_cell} клеток' if self.quantity_cell > 0 \
            else 'Клеток в организме нет'

    def make_order(self, quantity_items_line):
        str_order = ''
        score = 0
        quantity_lines = math.ceil(self.quantity_cell / quantity_items_line)
        for lines in range(0, quantity_lines):
            for item in range(0, quantity_items_line):
                if score == self.quantity_cell:
                    break
                str_order += '*'
                score += 1
            if score != self.quantity_cell:
                str_order += '\n'
        return str_order


a = OrganismCell(15)
print(a)
print()

b = OrganismCell(8)
print(b)
print()

c_add = OrganismCell(a + b)
print(c_add)
print()

c_sub = OrganismCell(a - b)
print(c_sub)
print()

c_mul = OrganismCell(a * b)
print(c_mul)
print()

c_truediv = OrganismCell(a / b)
print(c_truediv)
print()

print(a.make_order(4))