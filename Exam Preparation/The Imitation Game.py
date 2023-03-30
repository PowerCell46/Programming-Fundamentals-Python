encrypted_message = str(input())
encrypted_message = [letter for letter in encrypted_message]

while True:
    current_message = str(input())
    if current_message == "Decode":
        break
    current_message = current_message.split("|")

    if current_message[0] == "Move":
        counter = int(current_message[1])
        while counter > 0:
            counter -= 1
            current_element = encrypted_message.pop(0)
            encrypted_message.append(current_element)

    if current_message[0] == "Insert":
        index = int(current_message[1])
        value = current_message[2]
        encrypted_message.insert(index, value)
        encrypted_message = ''.join(encrypted_message)
        encrypted_message = [letter for letter in encrypted_message]
    if current_message[0] == "ChangeAll":
        substring = current_message[1]
        replacement = current_message[2]
        changed_message = "".join(encrypted_message)
        while substring in changed_message:
            changed_message = changed_message.replace(substring, replacement)
        encrypted_message = [letter for letter in changed_message]

print(f'The decrypted message is: {"".join(encrypted_message)}')
