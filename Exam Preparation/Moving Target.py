sequence_of_targets = input().split(" ")
sequence_of_targets = [int(num) for num in sequence_of_targets]


while True:
    current_input = input()
    if current_input == "End":
        sequence_of_targets = [str(num) for num in sequence_of_targets]
        print("|".join(sequence_of_targets))
        break
    current_input = current_input.split(" ")

    if current_input[0] == "Shoot":
        index = int(current_input[1])
        power = int(current_input[2])
        if 0 <= index < len(sequence_of_targets):
            value = sequence_of_targets[index]
            value -= power
            if value <= 0:
                sequence_of_targets.pop(index)
            else:
                sequence_of_targets[index] = value

    elif current_input[0] == "Add":
        index = int(current_input[1])
        value = int(current_input[2])
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets.insert(index, value)
        else:
            print(f'Invalid placement!')

    elif current_input[0] == "Strike":
        index = int(current_input[1])
        radius = int(current_input[2])
        if index - radius >= 0 and index + radius < len(sequence_of_targets):
            pops = radius * 2 + 1
            starting_index = index - radius
            while pops > 0:
                sequence_of_targets.pop(starting_index)
                pops -= 1
        else:
            print("Strike missed!")
