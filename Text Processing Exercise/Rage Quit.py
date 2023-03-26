cursed_word = str(input())
index = 0
unique_list = []
current_string = ""
final_string = ""

while index < len(cursed_word):
    current_digit = cursed_word[index]
    if 47 < ord(current_digit) < 58:
        index += 1
        while index < len(cursed_word) and 47 < ord(cursed_word[index]) < 58:
            current_digit = current_digit + cursed_word[index]
            index += 1
        index -= 1
        final_string += current_string * int(current_digit)
        current_string = ""
    else:
        if current_digit.lower() not in unique_list:
            unique_list.append(current_digit.lower())
        current_string += current_digit
    index += 1

print(f'Unique symbols used: {len(unique_list)}')
print(final_string.upper())
