list_of_nums = input().split(", ")
list_of_numbers = [int(number) for number in list_of_nums]
current_boundary = 0
while len(list_of_numbers) > 0:
    current_boundary += 10
    current_list = [number for number in list_of_numbers if number <= current_boundary]
    print(f'Group of {current_boundary}' + "'s:", current_list)
    while len(current_list) > 0:
        current_remove = current_list[0]
        list_of_numbers.remove(current_remove)
        current_list.remove(current_remove)
