import re

input_string = str(input())
pattern = r'([\||#]{1})([A-Za-z ]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1'

results = re.findall(pattern, input_string)
total_calories = 0

for current_list in results:
    current_list = list(current_list)
    total_calories += int(current_list[3])

print(f'You have food to last you for: {total_calories // 2000} days!')

for current_list in results:
    current_list = list(current_list)
    print(f'Item: {current_list[1]}, Best before: {current_list[2]}, Nutrition: {current_list[3]}')
