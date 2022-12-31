length_of_the_train = int(input())
wagons_list = []
for index in range(0, length_of_the_train):
    wagons_list.append(0)

while True:
    current_command = (str(input()))
    if current_command == "End":
        break
    current_command = current_command.split()
    command = current_command.pop(0)
    if command == "add":
        people = int(current_command.pop(0))
        value = wagons_list[len(wagons_list) - 1] + people
        wagons_list[len(wagons_list) - 1] = value
    elif command == "insert":
        index = int(current_command.pop(0))
        people_1 = int(current_command.pop(0))
        value_1 = wagons_list[index] + people_1
        wagons_list[index] = value_1
    elif command == "leave":
        index_1 = int(current_command.pop(0))
        people_2 = int(current_command.pop(0))
        value_2 = wagons_list[index_1] - people_2
        if value_2 < 0:
            value_2 = 0
        wagons_list[index_1] = value_2

print(wagons_list)
