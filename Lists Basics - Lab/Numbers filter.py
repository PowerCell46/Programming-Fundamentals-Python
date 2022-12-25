number_n = int(input())
number_list = []

for i in range(0, number_n):
    current_num = int(input())
    number_list.append(current_num)

operation = str(input())
second_list = []

if operation == "even":
    for index in range(0, len(number_list)):
        current_num = number_list[index]
        if current_num % 2 == 0:
            second_list.append(current_num)
elif operation == "odd":
    for index in range(0, len(number_list)):
        current_num = number_list[index]
        if current_num % 2 != 0:
            second_list.append(current_num)
elif operation == "negative":
    for index in range(0, len(number_list)):
        current_num = number_list[index]
        if current_num < 0:
            second_list.append(current_num)
elif operation == "positive":
    for index in range(0, len(number_list)):
        current_num = number_list[index]
        if current_num >= 0:
            second_list.append(current_num)

print(second_list)