def read_file(name_file):
    with open(name_file, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(name_file, text):
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(text)


translate_dict = {'One': 'Один',
                  'Two': 'Два',
                  'Three': 'Три',
                  'Four': 'Четыре',}

file_text_str = read_file('task4.txt')

for key, value in translate_dict.items():
    file_text_str = file_text_str.replace(key, value)

print(file_text_str)

write_file('task4_translate.txt', file_text_str)