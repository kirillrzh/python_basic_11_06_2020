from itertools import count

def fibo_gen_2():
    factorial = 1
    for i in count(1):
        if i < 16:
            factorial *= i
            print(f'Факториал числа {i}! = {factorial}')
        else:
            break
    yield factorial

print(fibo_gen_2())

for i in fibo_gen_2():
    print(i)