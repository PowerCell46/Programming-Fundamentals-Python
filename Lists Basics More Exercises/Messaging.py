sequence_of_numbers = input().split()
list_of_sums = []
input_string = input()

for i in range(0, len(sequence_of_numbers)):
    current_sequence = sequence_of_numbers[i]
    current_sum = 0
    for index in range(0, len(current_sequence)):
        current_number = int(current_sequence[index])
        current_sum += current_number
    list_of_sums.append(current_sum)

string_list = [char for char in input_string]
print_output = ""

for i in range(0, len(list_of_sums)):
    current_sum = list_of_sums[i]
    while current_sum >= len(string_list):
        current_sum -= len(string_list)
    print_output += string_list[current_sum]
    string_list.pop(current_sum)

print(print_output)
