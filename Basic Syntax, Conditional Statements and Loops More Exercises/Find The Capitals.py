input_word = str(input())
print_list = []

for index in range(0, len(input_word)):
    current_digit = input_word[index]
    for char in range(65, 91):
        if current_digit == chr(char):
            print_list.append(index)

print(print_list)
