list_of_nums = input().split()
left_one = 0
right_one = 0

while True:
    if len(list_of_nums) == 1:
        break
    left_num = int(list_of_nums.pop(0))
    right_num = int(list_of_nums.pop())

    if right_num == 0:
        right_one -= (right_one / 100) * 20
    if left_num == 0:
        left_one -= (left_one / 100) * 20
    left_one += left_num
    right_one += right_num

if left_one < right_one:
    print(f'The winner is left with total time: {left_one:.1f}')
elif right_one < left_one:
    print(f'The winner is right with total time: {right_one:.1f}')
