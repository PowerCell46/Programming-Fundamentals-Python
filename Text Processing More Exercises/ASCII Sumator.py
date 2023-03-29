number_of_lines = int(input())
name = ""
age = ""

while number_of_lines > 0:
    number_of_lines -= 1
    current_line = str(input())

    for index, char in enumerate(current_line):

        if char == "@":
            index += 1
            while True:
                char = current_line[index]
                if char == "|":
                    break
                name += char
                index += 1

        if char == "#":
            index += 1
            while True:
                char = current_line[index]
                if char == "*":
                    break
                age += char
                index += 1

    print(f'{name} is {age} years old.')
    name = ""
    age = ""
