last_number = int(input())
if last_number == 1:
    print("1")
elif last_number == 2:
    print("1 1")
elif last_number == 3:
    print("1 1 2")
else:
    numbers_list = [1, 1, 2]

    current_number = 0
    index = 3

    while True:
        current_number = numbers_list[index - 3] + numbers_list[index - 2] + numbers_list[index - 1]
        if len(numbers_list) == last_number:
            break
        numbers_list.append(current_number)
        index += 1

    print_list = []

    for i in range(0, len(numbers_list)):
        current_number = numbers_list[i]
        print_list.append(str(current_number))

    print(" ".join(print_list))
