#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ret = 0
    output = ""

    for i in range(x):
        try:
            output += "{}".format(my_list[i])
            ret += 1
        except IndexError:
            break

    print(output)
    return ret

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, 5)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, 7)
print("nb_print: {:d}".format(nb_print))

