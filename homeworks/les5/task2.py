def read_file(name_file):

    with open(name_file, 'r', encoding='utf-8') as file:
        print(file.read())


def quantity_lines_in_file(name_file):

    with open(name_file, 'r', encoding='utf-8') as file:
        score = 0
        while True:
            content = file.readline()
            if not content:
                break
            score += 1
        return score


def quantity_word_in_file(name_file):

    with open(name_file, 'r', encoding='utf-8') as file:
        check_word_sum_list = []
        while True:
            content = file.readline()
            if not content:
                break
            check_word_sum_list.extend(content.split())
        return len(check_word_sum_list)


def quantity_symbols_in_file(name_file):

    with open(name_file, 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.split()
        content = ''.join(content)
        return len(content)


def quantity_el_in_file(name_file):

    with open(name_file, 'r', encoding='utf-8') as file:
        str_test = ''
        while True:
            content = file.readline()
            if not content:
                break
            str_test += content
        return len(str_test.replace('\n', ''))


def quantity_element_in_file(name_file):

    with open(name_file, 'r', encoding='utf-8') as file:
        content = file.read()
        return len(content)


def str_info_for_text_file(name_file):
    print(f'Количество строк в файле - {quantity_lines_in_file(name_file)};\n'
          f'Количество слов в файле - {quantity_word_in_file(name_file)};\n'
          f'Количество символов в файле без пробелов и операторов новых строк - {quantity_symbols_in_file(name_file)};\n'
          f'Количество элементов в файле c пробелами и без операторов новых строк - {quantity_el_in_file(name_file)};\n'
          f'Количество элементов в файле c пробелами и операторами новых строк - {quantity_element_in_file(name_file)}.')


read_file('task2.txt')
print()
str_info_for_text_file('task2.txt')
print()