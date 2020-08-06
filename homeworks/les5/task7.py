import json

with open('task7.txt', 'r', encoding='utf-8') as file:
    result_dict = {}
    all_dict_firm = {}
    while True:
        line_list = file.readline().split()
        if not line_list:
            break
        line_list[0] = '"' + line_list[0] + '"'
        key_list = []
        for i in range(0, 2):
            key_list.append(line_list[i])
        key = ' '.join(reversed(key_list))
        average_firm = float(line_list[2]) - float(line_list[3])
        if average_firm > 0:
            result_dict[key] = average_firm
        all_dict_firm[key] = average_firm

    score = 0
    average_all_list = []
    average_dict = {}
    for key_2, value in result_dict.items():
        score += 1
        average_all_list.append(value)
    average_profit = sum(average_all_list) / score

    average_dict['average_profit'] = average_profit

    result_list = []
    result_list.append(all_dict_firm)
    result_list.append(average_dict)

    print(result_list)

with open('JSON_TASK7.json', 'w', encoding='utf-8') as file:
    json.dump(result_list, file)

with open('JSON_TASK7.json', 'r', encoding='utf-8') as file:
    open_result_list_json = json.load(file)
    print(open_result_list_json)