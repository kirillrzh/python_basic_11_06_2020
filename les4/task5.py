import functools
print(functools.reduce(lambda arg_1, arg_2: arg_1 + arg_2, [i for i in range(100, 1001) if i % 2 == 0]))