import math

string_of_numbers = str(input())
numbers_list = string_of_numbers.split()
print_list = []

for i in range(0, len(numbers_list)):
    current_num = int(numbers_list[i])
    if current_num > 0:
        current_num = current_num * -1
        print_list.append(current_num)
    elif current_num < 0:
        current_num = math.fabs(current_num)
        current_num = math.trunc(current_num)
        print_list.append(current_num)
    elif current_num == 0:
        print_list.append(current_num)

print(print_list)