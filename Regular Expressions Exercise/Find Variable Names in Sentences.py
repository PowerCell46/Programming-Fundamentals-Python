import re

input_string = str(input())
pattern = r'\b[_]{1}[A-Z|a-z|0-9]+\b'
result = re.findall(pattern, input_string)

final_result = []

for current_result in result:
    final_current_result = ""
    current_result = [letter for letter in current_result]
    for i in current_result:
        if i != "_":
            final_current_result += i
    final_result.append(final_current_result)

print(",".join(final_result))
