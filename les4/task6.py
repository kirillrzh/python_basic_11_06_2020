from itertools import count
from itertools import cycle

# -----------------------------------------------------a-------------------------------------------------------------

start_number_count = 1
step_count = 7

start_number_list = []

for i in count(start_number_count, step_count):
    if i > 100:
        break
    start_number_list.append(i)

print(start_number_list)

# -----------------------------------------------------b-------------------------------------------------------------

score = 0

second_list = []

for i in cycle(start_number_list):
    score += 1
    if score <= 7:
        print(i)
        second_list.append(i)
    else:
        break

print(f'Всего повторено {second_list}.')

print(f'Сумма от цикла повторений равна {sum(second_list)}.')