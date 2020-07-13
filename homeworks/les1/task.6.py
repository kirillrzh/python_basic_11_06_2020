a = input('Введите результаты пробежки первого дня в км \n')
b = input('Введите общий желаемый результат в км \n')
a = int(a)
b = int(b)
result_days = 1
result_km = a
while result_km < b:
        a = a + (0.1 * a)
        result_days += 1
        result_km = a
print(f'Вы достигнете требуемых показателей на %.d день' % result_days)