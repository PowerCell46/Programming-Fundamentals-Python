dragons = {}
dragon_types = {}
number_of_dragons = int(input())

while number_of_dragons > 0:
    number_of_dragons -= 1
    current_input = input()
    current_input = current_input.split(" ")
    dragon_type = current_input[0]
    dragon_name = current_input[1]
    damage = (current_input[2])
    if damage == "null":
        damage = 45
    else:
        damage = int(current_input[2])
    health = (current_input[3])
    if health == "null":
        health = 250
    else:
        health = int(current_input[3])
    armor = (current_input[4])
    if armor == "null":
        armor = 10
    else:
        armor = int(current_input[4])

    dragon_name = dragon_type + ":" + dragon_name
    dragons[dragon_name] = {}
    dragons[dragon_name][damage] = {}
    dragons[dragon_name][damage][health] = armor
    if dragon_type not in dragon_types.keys():
        dragon_types[dragon_type] = {}
        dragon_types[dragon_type][dragon_name] = {}
    else:
        dragon_types[dragon_type][dragon_name] = {}

dragon_type_stats = {}

for current_type in dragon_types:
    counter = 0
    t_damage = 0
    t_health = 0
    t_armor = 0
    for nameKey, dictionary in dragons.items():
        nameKey = nameKey.split(":")
        current_dragon_type = nameKey[0]
        if current_type == current_dragon_type:
            counter += 1
            current_damage = list(dragons[":".join(nameKey)].keys())
            current_damage = current_damage[0]
            t_damage += current_damage
            current_health = list(dragons[":".join(nameKey)][current_damage].keys())
            current_health = current_health[0]
            t_health += current_health
            current_armor = list(dragons[":".join(nameKey)][current_damage].values())
            current_armor = current_armor[0]
            t_armor += current_armor
    t_damage /= counter
    t_health /= counter
    t_armor /= counter
    current_dragon_type_stats = f'({t_damage:.2f}/{t_health:.2f}/{t_armor:.2f})'
    dragon_type_stats[current_type] = current_dragon_type_stats

for print_type in dragon_type_stats:
    print(f'{print_type}::{dragon_type_stats[print_type]}')
    print_type_names_list = []
    for nameKey, dictionary in dragons.items():
        nameKey = nameKey.split(":")
        current_type = nameKey[0]
        if current_type == print_type:
            print_type_names_list.append(":".join(nameKey))
    print_type_names_list.sort()
    for print_dragon in print_type_names_list:
        print_damage = list(dragons[print_dragon].keys())
        print_health = list(dragons[print_dragon][print_damage[0]].keys())
        print_armor = list(dragons[print_dragon][print_damage[0]].values())
        print_dragon = print_dragon.split(":")
        print(f'-{print_dragon[1]} -> damage: {print_damage[0]}, health: {print_health[0]}, armor: {print_armor[0]}')

