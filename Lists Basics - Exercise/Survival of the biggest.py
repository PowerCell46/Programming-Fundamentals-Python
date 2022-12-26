numbers = str(input())
number_n = int(input())
numbers_list = numbers.split()
duplicate_list = []

for i in range(0, len(numbers_list)):
    current_num = int(numbers_list[i])
    duplicate_list.append(current_num)
duplicate_list.sort()

while True:
    number_n -= 1
    if number_n == -1:
        break
    duplicate_list.pop(0)

final_print_list = []
for i in range(0, len(numbers_list)):
    current_num = int(numbers_list[i])
    if duplicate_list.count(current_num) > 0:
        final_print_list.append(str(current_num))

print(", ".join(final_print_list))