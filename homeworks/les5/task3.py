def create_dict_in_file(name_file):
    with open(name_file, 'r', encoding='utf-8') as file:
        all_el_list = file.readlines()
        person_list = []
        for i in range(0, len(all_el_list)):
            person_list.append(all_el_list[i].split())
        dict_person = {person_list[key][0]: float(person_list[salary][1]) for key, salary
                       in zip(range(0, (len(person_list) - 1)), range(0, (len(person_list) - 1)))}
        return dict_person


def salary_check_bedolagi(person_salary_dict):
    bedolagi_list = []
    for key, value in person_salary_dict.items():
        if value < 20000:
            bedolagi_list.append(key)
    return bedolagi_list


def func_average_salary(person_salary_dict):
    score = 0
    salary_list = []
    for key, value in person_salary_dict.items():
        score += 1
        salary_list.append(value)
    average_salary = round(sum(salary_list) / score, 2)
    return average_salary


def print_staff_salary_info(name_file):
    person_salary_dict = create_dict_in_file(name_file)
    bedolagi_list = salary_check_bedolagi(person_salary_dict)
    average_salary = func_average_salary(person_salary_dict)
    bedolagi_str = ', '.join(bedolagi_list)
    print(f'У следующих сотрудников зарплата мнее 20 тыс.руб: {bedolagi_str}. Средняя зарплата по '
          f'компании составила {average_salary}')

print_staff_salary_info('task3.txt')