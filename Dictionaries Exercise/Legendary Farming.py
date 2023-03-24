legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
end_the_game = False

while True:
    currentInput = str(input()).split(" ")
    index = 0
    while index < len(currentInput):
        current_quantity = int(currentInput[index])
        index += 1
        current_items = str(currentInput[index]).lower()
        index += 1

        if current_items in legendary_items.keys():
            previous_value = legendary_items[current_items]
            legendary_items[current_items] = (previous_value + current_quantity)
            if (previous_value + current_quantity) >= 250:
                if current_items == "shards":
                    print("Shadowmourne obtained!")
                    legendary_items[current_items] = (previous_value + current_quantity) - 250
                    end_the_game = True
                    break
                elif current_items == "fragments":
                    print('Valanyr obtained!')
                    legendary_items[current_items] = (previous_value + current_quantity) - 250
                    end_the_game = True
                    break
                elif current_items == "motes":
                    print("Dragonwrath obtained!")
                    legendary_items[current_items] = (previous_value + current_quantity) - 250
                    end_the_game = True
                    break
        else:
            legendary_items[current_items] = current_quantity
    if end_the_game:
        break

for key, value in legendary_items.items():
    print(f'{key}: {value}')
