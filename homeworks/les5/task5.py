def write_file(name_file, text):
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(text)


def read_file(name_file):
    with open(name_file, 'r', encoding='utf-8') as file:
        return file.read()


text_for_write = '7 7 7 7 7 7 7 7'

write_file('task5.txt', text_for_write)

text_file_str = read_file('task5.txt')

text_list = text_file_str.split()
text_list_float = []
for i in text_list:
    if i.isdigit():
        text_list_float.append(float(i))

print(f'Сумма чисел в файле {sum(text_list_float)}')