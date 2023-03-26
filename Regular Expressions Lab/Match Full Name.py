import re

text = str(input())

search_pattern = r'\b[A-Z]{1}[a-z]{1,} [A-Z]{1}[a-z]{1,}\b'

result = re.findall(search_pattern, text)
print(" ".join(result))
