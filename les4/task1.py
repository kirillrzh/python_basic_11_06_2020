import sys

def salary(staff_member, production_in_hours, price_in_hours, premium):

    salary_staff_member = (float(production_in_hours) * float(price_in_hours)) + float(premium)
    print(f'\nЗарплата сотрудника {staff_member} составил {salary_staff_member}. Ставка в час {price_in_hours}, '
          f'отработано часов {production_in_hours}, премия {premium}.\n')

try:
    script_name, staff_member, production_in_hours, price_in_hours, premium = sys.argv
except ValueError:
    print('\nНе все параметры были ввведены! Вводите в следующем порядке:\n'
          '\nПервый параметр: script_name имя файла. Пример (****.ру);\n'
          'Второй параметр: staff_member Фамилия и инициалы сотрудника. Пример (Иванов.И.И.);\n'
          'Третий параметр: production_in_hours - выработка в часах. Пример (5);\n'
          'Четвертый параметр: price_in_hours - ставка в час. Пример (250);\n'
          'Пятый параметр: premium - премия. Пример (3000);\n'
          '\nПример полной команды (python pphw4.1.py иванов.и.и 5 250 300)\n')
else:
    salary(staff_member, production_in_hours, price_in_hours, premium)