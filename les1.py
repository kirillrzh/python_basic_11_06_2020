"""
int - это целое число
float - это дробное
str - это строка
bool - boolean всего 2 значения истина или ложь
"""


catalog_id_1 = 14  # Это коментарий
catalog_id_2 = 15
my_float = 12.134
my_str1 = 'Это строка 1'
my_str2 = "Это тоже строка 2"
my_str3 = """то строка из
множества
строк"""

my_str4 = 'Нужно выделить "Термин"'
my_str5 = "Нужно выделить \"Термин\""


#age = 33

#if  age >= 18:
#    print('Доступ разрешен')
#    if age == 33:
#        print('xxx')
#elif age >= 16:
#    print('ограниченный доступ')
#else:
#    print('Доступ запрещен')

#while True:
#    age = input('Введите возраст\n')
#    if not age.isdigit():
#        print('возраст должен быть числом')
#        continue
#    age = int(age)
#    break


#if age >= 18:
#    print('Доступ разрешен во все разделы включая xxx')
#elif age >= 16:
#    print('Доступ разрешен во все разделы')
#elif age >= 8:
#    print('Доступ разрешен в раздел мультики')
#else:
#    print('Доступ запрещен')


name = 'USER'
surname = 'LAMER'
age = 16
'Пример User, тебе 16 лет твоя фамилия Lamer'
result = 'Пример {n} тебе {a}твоя фамилия {s}.format(n=name, a=age, s=surname)'
f_result = f'Пример {name}, тебе {age} лет твоя фамилия {surname}, {2020 - age} года рождения'
print(f_result)