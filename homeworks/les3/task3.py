def sum_two_max(arg_1, arg_2, arg_3):
    list_check = [arg_1, arg_2, arg_3]
    firs_arg = list_check.pop(list_check.index(max(list_check)))
    second_arg = list_check.pop(list_check.index(max(list_check)))
    return firs_arg + second_arg

sum_test = sum_two_max(4, 2, 3)

print(sum_test)