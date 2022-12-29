sequence_of_numbers = (str(input())).split()
print_list = []


for i in range(0, len(sequence_of_numbers)):
    current_num = int(sequence_of_numbers[i])
    print_list.append(current_num)

print_list =  sorted(print_list)

print(print_list)
