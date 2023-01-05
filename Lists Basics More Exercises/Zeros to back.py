list_of_nums = input().split(", ")
list_of_numbers = [int(num) for num in list_of_nums]

for i in range(0, len(list_of_numbers)):
    current_num = int(list_of_numbers[i])
    if current_num == 0:
        list_of_numbers.remove(0)
        list_of_numbers.append(0)

print(list_of_numbers)
