with open('PPHW5.1.txt', 'w', encoding='utf-8') as file:
    while True:
        content = input('Введите строку для записи в файл - ')

        if not content:
            break

        content += '\n'
        file.write(content)

with open('PPHW5.1.txt', 'r', encoding='utf-8') as file:
    print(file.read())