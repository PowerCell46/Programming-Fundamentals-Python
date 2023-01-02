number_of_characters = int(input())
sum = 0
while True:
    number_of_characters -= 1
    if number_of_characters == -1:
        break
    current_character = str(input())
    current_value = ord(current_character)
    sum += current_value

print(f'The sum equals: {sum}')
