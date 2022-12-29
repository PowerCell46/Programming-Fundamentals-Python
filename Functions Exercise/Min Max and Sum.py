list_of_nums = (input()).split()
new_list_of_nums = []
sum = 0
for i in range(0, len(list_of_nums)):
    current_num = int(list_of_nums[i])
    new_list_of_nums.append(current_num)
    sum += current_num

print(f'The minimum number is {min(new_list_of_nums)}')
print(f'The maximum number is {max(new_list_of_nums)}')
print(f'The sum number is: {sum}')
