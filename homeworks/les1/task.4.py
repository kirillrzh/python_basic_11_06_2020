n = input('Введите целое положительное число \n')
n = abs(int(n))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print('Самая большая цифра в числе ', max)
        break