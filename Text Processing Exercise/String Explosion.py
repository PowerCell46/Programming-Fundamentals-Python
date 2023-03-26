explosion_string = str(input())
explosion_string_list = [letter for letter in explosion_string]

index = 0

while index < len(explosion_string_list):
    current_letter = explosion_string_list[index] # буквата, която ще проверяваме

    if current_letter == ">":
        index += 1
        if index == len(explosion_string_list):
            break
        power_of_the_bomb = int(explosion_string_list[index]) # силата на бомбата
        explosion_string_list.pop(index)
        power_of_the_bomb -= 1 # pop-нали сме числото и намаляваме силата с единица
        if power_of_the_bomb == 0:
            index -= 1

        while power_of_the_bomb > 0 and index < len(explosion_string_list):
            current_letter = explosion_string_list[index] # взимаме следващата буква
            if current_letter == ">":
                index += 1
                if index == len(explosion_string_list):
                    break
                power_of_the_bomb += int(explosion_string_list[index])
                explosion_string_list.pop(index)
                power_of_the_bomb -= 1 # pop-ваме силата на бомбата и намаляваме силата и с единица
                if power_of_the_bomb == 0:
                    index -= 1
            else:
                explosion_string_list.pop(index)
                power_of_the_bomb -= 1
                if power_of_the_bomb == 0:
                    index -= 1

    if index == len(explosion_string_list):
        break
    index += 1

print("".join(explosion_string_list))
