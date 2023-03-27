import re

input_nums = str(input())

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

result = re.finditer(pattern, input_nums)

print_string = ""
for match in result:
    print_string += match.group() + " "

print(print_string)
