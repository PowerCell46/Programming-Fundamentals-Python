import re

print_string = ""
current_input = str(input())

while True:
    if current_input:
        pattern = r'\d+'
        numbers = re.findall(pattern, current_input)
        if len(numbers) > 0:
            print_string += " ".join(numbers) + " "
    else:
        break
    current_input = str(input())

print(print_string)
