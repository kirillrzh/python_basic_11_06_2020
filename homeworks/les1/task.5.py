revenue = input('Введите выручку фирмы \n')
revenue = float(revenue)
costs = input('Введите издержки фирмы \n')
costs = float(costs)
if revenue > costs:
    print(f'Фирма работает с прибылью. Рентабельность выручки составила {revenue / costs:.2f}')
    staff = input('Введите количество сотрудников фирмы \n')
    staff = int(staff)
    print(f"прибыль в расчете на одного сторудника составила: \n {revenue / staff:.2f}")
elif revenue == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")