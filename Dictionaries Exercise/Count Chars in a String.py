input_line = str(input())
input_line = [*input_line]

count_chars_dict = {}

for letter in input_line:
    if letter != " ":
        if letter in count_chars_dict.keys():
            count_chars_dict[letter] += 1
        else:
            count_chars_dict[letter] = 1

for key in count_chars_dict.keys():
    print(f'{key} -> {count_chars_dict[key]}')
