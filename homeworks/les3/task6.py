import re

def int_func(users_str):

    result_list = []

    for i in users_str.split():
        result_list.append(i.capitalize())

    result_str = ' '.join(result_list)

    print(result_str)


def check_lat_lower_symbols():

    while True:
        users_str = input('Введите строку содержащую только латинские символы - ').lower()

        if re.search(r'[^a-z ]', users_str):
            print('Cтрока должна содерджать только латинские символы!')
        else:
            return users_str


def int_func_two(users_str):

    result_list = []

    for i in users_str.split():
        result_list.append(i.capitalize())

    print(*result_list)

int_func(check_lat_lower_symbols())

int_func(check_lat_lower_symbols())

int_func_two(check_lat_lower_symbols())