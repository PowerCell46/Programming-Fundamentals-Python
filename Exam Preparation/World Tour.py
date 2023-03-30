stops = str(input())
stops = [letter for letter in stops]

while True:
    current_input = str(input())
    if current_input == "Travel":
        break
    current_input = current_input.split(":")

    if current_input[0] == "Add Stop":
        index = int(current_input[1])
        string = current_input[2]
        if 0 <= index < len(stops):
            stops.insert(index, string)
            stops = "".join(stops)
            stops = [letter for letter in stops]
        print("".join(stops))

    elif current_input[0] == "Remove Stop":
        start_index = int(current_input[1])
        end_index = int(current_input[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            pops = end_index - start_index + 1
            while pops > 0:
                stops.pop(start_index)
                pops -= 1
        print("".join(stops))

    elif current_input[0] == "Switch":
        old_string = current_input[1]
        new_string = current_input[2]
        stops = "".join(stops)
        if old_string in stops:
            stops = stops.split(old_string)
            stops = new_string.join(stops)
        stops = [letter for letter in stops]
        print("".join(stops))

print(f'Ready for world tour! Planned stops: {"".join(stops)}')
