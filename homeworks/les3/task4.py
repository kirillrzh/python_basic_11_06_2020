def check_numbers_float(text):

    while True:
        number = input(text)
        if number.isdigit():
            return float(number)
        print('Введите числовое значение!')

def check_numbers_negative(text):

    while True:

        request_text = 'Введите отрицательное число'

        try:
            number = int(input(text))
        except ValueError:
            print(request_text)
            continue

        if number < 0:
            return number
        print(request_text)


def x_in_degree_y(x, y):
    return x ** y


arg_1_positive = check_numbers_float('Введите число которое будем возводить в степень - ')

arg_1_negative = check_numbers_negative('Введите степень (отрицательное число) - ')

result = x_in_degree_y(arg_1_positive, arg_1_negative)

print(f'Если возвести число {arg_1_positive} в степень {arg_1_negative}, получим число {result}')