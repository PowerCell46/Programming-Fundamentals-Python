number_of_lines = int(input())
plants_dictionary = {}

while number_of_lines > 0:
    number_of_lines -= 1
    current_input = str(input()).split("<->")
    plant = current_input[0]
    rarity = int(current_input[1])
    plants_dictionary[plant] = {}
    plants_dictionary[plant][rarity] = 0

while True:
    current_input = str(input())
    if current_input == "Exhibition":
        break
    current_input = current_input.split(": ")

    if current_input[0] == "Rate":
        current_input = current_input[1].split(" - ")
        plant = current_input[0]
        rating = int(current_input[1])
        if plant in plants_dictionary.keys():
            rarity = list(plants_dictionary[plant].keys())
            rarity = int(rarity[0])
            previous_rating = list(plants_dictionary[plant].values())
            if previous_rating[0] != 0:
                rating = ((previous_rating[0]) + rating) / 2
                plants_dictionary[plant][rarity] = rating
            else:
                plants_dictionary[plant][rarity] = rating
        else:
            print('error')

    elif current_input[0] == "Update":
        current_input = current_input[1].split(" - ")
        plant = current_input[0]
        if plant in plants_dictionary.keys():
            new_rarity = int(current_input[1])
            old_rarity = list(plants_dictionary[plant].keys())
            old_rarity = int(old_rarity[0])
            rating = list(plants_dictionary[plant].values())
            plants_dictionary[plant] = {}
            if len(rating) > 0:
                plants_dictionary[plant][new_rarity] = (rating[0])
            else:
                plants_dictionary[plant][new_rarity] = 0
        else:
            print("error")

    elif current_input[0] == "Reset":
        plant = current_input[1]
        if plant in plants_dictionary.keys():
            rarity = (list(plants_dictionary[plant].keys())[0])
            plants_dictionary[plant] = {}
            plants_dictionary[plant][rarity] = 0
        else:
            print(f'error')

print(f'Plants for the exhibition:')
for plant, dictionary in plants_dictionary.items():
    for rarity, rating in dictionary.items():
        print(f'- {plant}; Rarity: {rarity}; Rating: {rating:.2f}')
