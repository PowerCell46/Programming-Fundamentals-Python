integer = int(input()) + 1

for i in range(1, integer):
    current_num = i
    current_num = str(current_num)
    sum = 0
    for index in range(0, len(current_num)):
        current_digit = current_num[index]
        current_digit = int(current_digit)
        sum += current_digit
    if sum == 5 or sum == 7 or sum == 11:
        print(f'{current_num} -> True')
    else:
        print(f'{current_num} -> False')