def sum_num_str():  # Функция суммирования цифр строк

    global result_summ
    global hub_numbers_sum
    global hub_users_str
    global hub_users_symbols
    stop_symbol = None

    while True:

        users_str = input('Введите строку чисел разделенную пробелами. Стоп символ "!" - ')

        hub_users_str.append(users_str)

        users_str = users_str.split()

        hub_users_symbols.append(tuple(users_str))

        work_list = []

        for i in users_str:
            check = check_numbers_float(i)
            if check == '!':
                stop_symbol = '!'
                break
            elif check != None:
                work_list.append(check)

        if work_list != []:
            hub_numbers_sum.extend(work_list)

        if hub_numbers_sum == []:
            print('Ни одного числа небыло введено')
        else:
            result_summ += sum(work_list)
            print(result_summ)

        # print(result_summ)

        if stop_symbol == '!':
            break


def check_numbers_float(arg_1):
    try:
        number = float(arg_1)
    except ValueError:
        if arg_1 == '!':
            return arg_1
    else:
        return number


result_summ = 0

hub_numbers_sum = []

hub_users_str = []

hub_users_symbols = []

sum_num_str()