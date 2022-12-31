input_number = str(input())
list = []

for index in range(0, len(input_number)):
    current_num = (input_number[index])
    current_num = int(current_num)
    list.append(current_num)

list = sorted(list)
sorted_list = []
for index in range(len(list) -1, -1, -1):
    current_num = list[index]
    sorted_list.append(current_num)

print(*sorted_list, sep="")
