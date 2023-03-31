targets_sequence = input().split(" ")
targets_sequence = [int(num) for num in targets_sequence]
shot_target_indexes = []

while True:
    current_input = input()
    if current_input == "End":
        break
    current_index = int(current_input)
    if current_index not in shot_target_indexes and 0 <= current_index < len(targets_sequence) :
        value = targets_sequence[current_index]
        targets_sequence[current_index] = -1
        shot_target_indexes.append(current_index)
        for i in range(0, len(targets_sequence)):
            current_value = targets_sequence[i]
            if current_value != -1:
                if current_value > value:
                    targets_sequence[i] = current_value - value
                elif current_value <= value:
                    targets_sequence[i] = current_value + value

targets_sequence = [str(num) for num in targets_sequence]
print(f'Shot targets: {len(shot_target_indexes)} -> {" ".join(targets_sequence)}')
