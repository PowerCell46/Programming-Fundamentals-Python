import math
numbers_list = (str(input())).split()
print_list = []

def absolute_values(value):
    value = math.fabs(value)
    print_list.append(value)

for i in range(0, len(numbers_list)):
    value = float(numbers_list[i])
    absolute_values(value)

print(print_list)