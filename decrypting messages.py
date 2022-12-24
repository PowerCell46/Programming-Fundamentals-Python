key = int(input())
number_of_lines = int(input())
print_text = ""
for  i in range(0, number_of_lines):
    current_digit = str(input())
    current_print = ord(current_digit) + key
    current_print = chr(current_print)
    print_text += current_print

print(print_text)