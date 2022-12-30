first_num = int(input())
second_num = int(input())
third_num = int(input())
list = []
list.append(first_num)
list.append(second_num)
list.append(third_num)
biggest_num = -100000

for index in range(0, 3):
    current_num = list[index]
    if current_num > biggest_num:
        biggest_num = current_num

print(biggest_num)
