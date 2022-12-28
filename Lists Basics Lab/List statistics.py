number_n = int(input())
positive_list = []
positive_count = 0
negative_list = []
negative_sum = 0

for index in range(0, number_n):
    current_num = int(input())
    if current_num > 0:
        positive_list.append(current_num)
        positive_count += 1
    elif current_num < 0:
        negative_list.append(current_num)
        negative_sum += current_num

print(positive_list)
print(negative_list)
print(f'Count of positives: {positive_count}')
print(f'Sum of negatives: {negative_sum}')