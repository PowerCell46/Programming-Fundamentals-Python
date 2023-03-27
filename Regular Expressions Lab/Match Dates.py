import re

dates = str(input())

pattern = r'([0-9]{2})\/([A-Z]{1}[a-z]{2})\/(\d{4})|([0-9]{2})-([A-Z]{1}[a-z]{2})-(\d{4})|([0-9]{2})[.]([A-Z]{1}[a-z]{2})[.](\d{4})'

result = re.findall(pattern, dates)

for match in result:
    current_match = []
    for i in match:
        if len(i) > 0:
            current_match.append(i)
            
    print(f'Day: {current_match[0]}, Month: {current_match[1]}, Year: {current_match[2]}')
