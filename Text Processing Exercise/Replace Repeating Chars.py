input_string = str(input())
input_string_list = [letter for letter in input_string]
index = 0
final_str = ""

while index < len(input_string_list):
    current_letter = input_string_list[index]
    final_str += current_letter
    index += 1
    if index == len(input_string_list):
        break
    next_letter = input_string_list[index]
    if current_letter == next_letter:
        while current_letter == next_letter:
            index += 1
            if index == len(input_string_list):
                break
            next_letter = input_string_list[index]
print(final_str)
