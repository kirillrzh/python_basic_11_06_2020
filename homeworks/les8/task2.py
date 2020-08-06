class DivisionByZero(Exception):
    def __str__(self):
        return 'На ноль делить нельзя!'


def division(private, divider):
    try:
        if divider == 0:
            raise DivisionByZero()
        return float(private) / float(divider)
    except ValueError:
        return 'Вводить можно только числа'
    except DivisionByZero as i:
        return i


print(division(5, 5))

print(division(5, 's'))

print(division(5, 0))