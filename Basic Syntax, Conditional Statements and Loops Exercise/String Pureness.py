number_of_strings = int(input())
while True:
    the_string_is_pure = True
    number_of_strings -= 1
    if number_of_strings == -1:
        break
    current_string = str(input())
    for index in range(0, len(current_string)):
        current_letter = current_string[index]
        if current_letter != "," and current_letter != "." and current_letter != "_":
            the_string_is_pure = True
        else:
            the_string_is_pure = False
            break
    if the_string_is_pure == True:
        print(f'{current_string} is pure.')
    elif the_string_is_pure == False:
        print(f'{current_string} is not pure!')
