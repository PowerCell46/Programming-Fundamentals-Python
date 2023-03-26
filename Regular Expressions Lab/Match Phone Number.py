import re
phone_numbers = str(input())

pattern = r'[+]359 2 [0-9]{3} [0-9]{4}\b|[+]359-2-[0-9]{3}-[0-9]{4}\b'

result = re.findall(pattern, phone_numbers)

print(", ".join(result))
