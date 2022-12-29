sequence_of_numbers = (str(input())).split()
even_nums_list = []

def even_numbers(sequence_of_numbers):
    for i in range(0, len(sequence_of_numbers)):
        current_num = int(sequence_of_numbers[i])
        if current_num % 2 == 0:
            even_nums_list.append(current_num)

even_numbers(sequence_of_numbers)

print(even_nums_list)
