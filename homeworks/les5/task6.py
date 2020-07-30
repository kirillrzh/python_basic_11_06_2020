with open('task6.txt', 'r', encoding='utf-8') as file:
    result_dict = {}
    while True:
        line_list = file.readline().split()
        if not line_list:
            break
        key = line_list.pop(0)[:-1]
        list_numbers = []
        for i_str in line_list:
            list_number = []
            for index in range(0, len(i_str)):
                if i_str[index].isdigit():
                    list_number.append(i_str[index])
            if list_number != []:
                number = float(''.join(list_number))
                list_numbers.append(number)
        value = sum(list_numbers)
        result_dict[key] = value
    print(result_dict)