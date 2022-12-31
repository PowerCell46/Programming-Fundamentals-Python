numbers_list = (str(input())).split(", ")
even_numbers_indexes_list = []

for i in range(0, len(numbers_list)):
    current_num = int(numbers_list[i])
    if current_num % 2 == 0:
        even_numbers_indexes_list.append(i)

print(even_numbers_indexes_list)
