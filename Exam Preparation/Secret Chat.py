concealed_message = str(input())
concealed_message = [letter for letter in concealed_message]

while True:
    current_input = str(input())
    if current_input == "Reveal":
        print(f'You have a new text message: {"".join(concealed_message)}')
        break
    current_input = current_input.split(":|:")

    if current_input[0] == "InsertSpace":
        index = int(current_input[1])
        concealed_message.insert(index, " ")
        print("".join(concealed_message))

    elif current_input[0] == "Reverse":
        substring = current_input[1]
        concealed_message = "".join(concealed_message)
        if substring in concealed_message:
            search_index = concealed_message.index(substring)
            pops = len(substring)
            concealed_message = [letter for letter in concealed_message]
            while pops > 0:
                concealed_message.pop(search_index)
                pops -= 1
            substring = [letter for letter in substring]
            substring.reverse()
            substring = "".join(substring)
            concealed_message = "".join(concealed_message)
            concealed_message += substring
            concealed_message = [letter for letter in concealed_message]
            print("".join(concealed_message))
        else:
            concealed_message = [letter for letter in concealed_message]
            print("error")

    elif current_input[0] == "ChangeAll":
        substring = current_input[1]
        replacement = current_input[2]
        concealed_message = "".join(concealed_message)
        concealed_message = concealed_message.split(substring)
        concealed_message = replacement.join(concealed_message)
        concealed_message = [letter for letter in concealed_message]
        print("".join(concealed_message))
