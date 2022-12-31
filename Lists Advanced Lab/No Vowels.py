input_word = str(input())
new_list = [x for x in range(0, len(input_word)) if input_word[x] != "a" and input_word[x] != "A" and input_word[x] != "I" and input_word[x] != "i" and input_word[x] != "e" and input_word[x] != "E" and input_word[x] != "o" and input_word[x] != "O" and input_word[x] != "u" and input_word[x] != "U" ]
print_str = ""
for i in range(0, len(new_list)):
    current_letter = input_word[new_list[i]]
    print_str += current_letter

print(print_str)
