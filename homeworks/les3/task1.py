def check_numbers(text):
    while True:
        number = input(text)
        if number.isdigit():
            return float(number)
        print('Введите числовое значение!')

def splitting(arg_1, arg_2):
    try:
        result = arg_1 / arg_2
    except ZeroDivisionError:
        return 'На ноль делить нельзя!!!'
    else:
        return result


arg_1 = check_numbers('Введите число которое будем делить - ')
arg_2 = check_numbers('Введите делитель - ')

print(splitting(arg_1, arg_2))
