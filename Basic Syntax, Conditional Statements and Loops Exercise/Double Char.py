while True:
    current_string = str(input())
    new_word = ""
    if current_string == "End":
        break
    elif current_string == "SoftUni":
        continue
    for index in range(0, len(current_string)):
        current_letter = current_string[index]
        new_word += current_letter
        new_word += current_letter
    print(new_word)
