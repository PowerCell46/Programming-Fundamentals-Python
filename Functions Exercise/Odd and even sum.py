current_num = str(input())

sum_of_odds = 0
sum_of_evens = 0

for i in range(0, len(current_num)):
    current_digit = int(current_num[i])
    if current_digit % 2 == 0:
        sum_of_evens += current_digit
    else:
        sum_of_odds += current_digit


print(f'Odd sum = {sum_of_odds}, Even sum = {sum_of_evens}')