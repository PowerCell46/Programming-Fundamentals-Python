import math

input_strings = input().split(" ")

while True:
    current_input = input()

    if current_input == "3:1":
        print(" ".join(input_strings))
        break
    current_input = current_input.split(" ")

    if current_input[0] == "merge":
        start_index = int(current_input[1])
        start_index = 0 if start_index < 0 else start_index
        end_index = int(current_input[2])
        end_index = len(input_strings) - 1 if end_index >= len(input_strings) else end_index
        new_line = []
        line = ""
        for i in range(0, len(input_strings)):
            if start_index <= i <= end_index:
                line += input_strings[i]
                if i == end_index:
                    new_line.append(line)
            else:
                new_line.append(input_strings[i])

        input_strings = new_line

    elif current_input[0] == "divide":
        working_index = int(current_input[1])
        number_of_partitions = int(current_input[2])
        working_string = input_strings[working_index]
        res = len(working_string) / number_of_partitions

        if res % 1 == 0:
            partitions_length = int(res)
            new_elements = []
            counter = 0
            current = ""
            for char in working_string:
                current += char
                counter += 1
                if counter == partitions_length:
                    new_elements.append(current)
                    current = ""
                    counter = 0

        else:
            partitions_length = math.floor(res)
            last_element_length = (len(working_string) - (partitions_length * number_of_partitions)) + partitions_length
            new_elements = []
            current = ""
            counter = 0

            for i in range(0, len(working_string) - last_element_length):
                current += working_string[i]
                counter += 1
                if counter == partitions_length:
                    new_elements.append(current)
                    current = ""
                    counter = 0

            for index in range((len(working_string) - 1), -1, -1):
                current += working_string[index]
                counter += 1
                if counter == last_element_length:
                    new_elements.append(current[::-1])
                    counter = 0
                    current = ""
                    break

        new_line = []
        for index in range(0, len(input_strings)):
            if index == working_index:
                new_line.extend(new_elements)
            else:
                new_line.append(input_strings[index])

        input_strings = new_line
