list_of_schedule = str(input()).split(", ")

while True:
    current_input = str(input())
    if current_input == "course start":
        break
    current_input = current_input.split(":")
    command = current_input[0]

    if command == "Add":
        if current_input[1] not in list_of_schedule:
            list_of_schedule.append(current_input[1])

    if command == "Insert":
        if current_input[1] not in list_of_schedule:
            list_of_schedule.insert(int(current_input[2]), current_input[1])

    if command == "Remove":
        if current_input[1] in list_of_schedule:
            while current_input[1] in list_of_schedule:
                search_index = list_of_schedule.index(current_input[1])
                list_of_schedule.pop(search_index)
            if (current_input[1] + "-Exercise") in list_of_schedule:
                while (current_input[1] + "-Exercise") in list_of_schedule:
                    search_index = list_of_schedule.index((current_input[1] + "-Exercise"))
                    list_of_schedule.pop(search_index)

    if command == "Swap":
        if current_input[1] in list_of_schedule and current_input[2] in list_of_schedule:
            first_index = list_of_schedule.index(current_input[1])
            second_index = list_of_schedule.index(current_input[2])
            list_of_schedule[first_index] = current_input[2]
            list_of_schedule[second_index] = current_input[1]
            if current_input[1] + "-Exercise" in list_of_schedule:
                search_index = list_of_schedule.index(current_input[1] + "-Exercise")
                list_of_schedule.pop(search_index)
                search_index1 = list_of_schedule.index(current_input[1])
                list_of_schedule.insert(search_index1 + 1, current_input[1] + "-Exercise")
            if current_input[2] + "-Exercise" in list_of_schedule:
                search_index = list_of_schedule.index(current_input[2] + "-Exercise")
                list_of_schedule.pop(search_index)
                search_index2 = list_of_schedule.index(current_input[2])
                list_of_schedule.insert(search_index2 + 1, current_input[2] + "-Exercise")

    if command == "Exercise":
        if (current_input[1] + "-Exercise") not in list_of_schedule:
            if current_input[1] in list_of_schedule:
                search_index = list_of_schedule.index(current_input[1])
                list_of_schedule.insert(search_index + 1, current_input[1] + "-Exercise")
            else:
                list_of_schedule.append(current_input[1])
                list_of_schedule.append(current_input[1] + "-Exercise")

for i in range(0, len(list_of_schedule)):
    print(f'{i + 1}.{list_of_schedule[i]}')
