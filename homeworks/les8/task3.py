import re


class NotNumber(Exception):
    def __str__(self):
        return 'Должно быть только число. Вещественное или целое. ' \
               'За искоренение букв, символов(кроме точки и запятой) и цифр их сообщников ' \
               'ведьмаку заплаченно чеканной монетой. Они не пройдут!'


def forming_list():
    """
    Функция которая принимает от пользователя числа как int так и float, и сохраняет их в список с сохранением
    типа числа. Косплексные числа и числа с смиволами не принимаются по прихоти автора.
    Ввод происходит по клавише интер пока пользователю не надоест.
    Стоп слово - "stop"
    :return:возврашает список соедржащий введенные числа с сохранением их типа.
    """
    result_list = []

    while True:
        try:
            element_list = input('Введиче число для заполнения списка, '
                                 'для прекрашенния введите "stop" - ').lower().replace(',', '.')
            if element_list == 'stop':
                break
            elif re.search(r'^[0-9.]+$', element_list):
                if len(element_list.split('.')) >= 2:
                    result_list.append(float(element_list))
                else:
                    result_list.append(int(element_list))
            else:
                raise NotNumber()
        except NotNumber as i:
            print(i)

    return result_list


a = forming_list()
print()
print(f'Итоговый список имеет следующий вид {a}.')