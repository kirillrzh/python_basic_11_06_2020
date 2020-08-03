from sys import argv

try:
    script_name, *args = argv
except ValueError:
    print('\nНе все параметры были ввведены! Вводите в следующем порядке:\n'
          '\nПервый параметр: script_name имя файла. Пример (****.ру);\n'
          'Далее параметры последовательности списка: *args а. Пример (300 2 12 44 1 1 4 10 7 1 78 123 55);\n'
          '\nПример полной команды (python pphw4.2.py 300 2 12 44 1 1 4 10 7 1 78 123 55)\n')
else:

    start_list = [*args]
    int_number_list = [int(i) for i in start_list if i.isdigit()]
    second_list = [int_number_list[i] for i in range(1, len(int_number_list)) if
                   int_number_list[i] > int_number_list[i - 1]]
    print(second_list)