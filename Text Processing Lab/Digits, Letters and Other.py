input_string = str(input())
input_string_list = [char for char in input_string]

nums = ""
letters = ""
others = ""

while len(input_string_list) > 0:
    current_digit = (input_string_list.pop(0))

    if 47 < ord(current_digit) < 58:
        nums += str(current_digit)
    elif 64 < ord(current_digit) < 91 or 96 < ord(current_digit) < 123:
        letters += current_digit
    else:
        others += current_digit

print(nums)
print(letters)
print(others)
