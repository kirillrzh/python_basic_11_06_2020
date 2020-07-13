while True:
    time = input('Введите время в секундах\n')
    if not time.isdigit():
        print('Секунды должны быть числом')
        continue
    time = int(time)
    break

hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")