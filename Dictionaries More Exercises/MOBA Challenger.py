player_pool = {}

while True:

    current_input = input()
    if current_input == "Season end":
        break

    if "->" in current_input:

        current_input = current_input.split(" -> ")
        current_player = current_input[0]
        current_position = current_input[1]
        current_skill = int(current_input[2])
        if current_player not in player_pool.keys():
            player_pool[current_player] = {}
            player_pool[current_player][current_position] = current_skill

        else:
            if current_position not in player_pool[current_player].keys():
                player_pool[current_player][current_position] = current_skill
            else:
                if current_skill > player_pool[current_player][current_position]:
                    player_pool[current_player][current_position] = current_skill

    else:
        current_input = current_input.split(" vs ")
        first_player = current_input[0]
        second_player = current_input[1]

        if first_player in player_pool.keys() and second_player in player_pool.keys():
            first_player_positions = player_pool[first_player].keys()
            second_player_positions = player_pool[second_player].keys()
            common_position = []
            for position in first_player_positions:
                if position in second_player_positions:
                    common_position.append(position)
                    break
            if len(common_position) > 0:
                first_player_skill = player_pool[first_player][common_position[0]]
                second_player_skill = player_pool[second_player][common_position[0]]

                if first_player_skill > second_player_skill:
                    del player_pool[second_player]
                else:
                    del player_pool[first_player]


total_points_dict = {}

for person in player_pool.keys():
    total_points_dict[person] = 0
    for position in player_pool[person].keys():
        total_points_dict[person] += player_pool[person][position]

total_points_dict = sorted(total_points_dict.items(), key=lambda x: (-x[1], x[0]))

for tuple in total_points_dict:
    print(f'{tuple[0]}: {tuple[1]} skill')
    current_person_dict = player_pool[tuple[0]]
    current_person_dict = sorted(current_person_dict.items(), key=lambda x: (-x[1], x[0]))
    for final_tuple in current_person_dict:
        print(f'- {final_tuple[0]} <::> {final_tuple[1]}')

