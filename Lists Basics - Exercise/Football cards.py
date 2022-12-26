team_A_list = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_B_list = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9","B-10", "B-11"]
red_cards_array = str(input()).split()
the_game_was_terminated = False

for i in range(0, len(red_cards_array)):
    current_card = red_cards_array[i]
    if current_card[0] == "A":
        if team_A_list.count(current_card) > 0:
            team_A_list.remove(current_card)
            if len(team_A_list) < 7:
                the_game_was_terminated = True
                print(f'Team A - {len(team_A_list)}; Team B - {len(team_B_list)}')
                print("Game was terminated")
                break
    elif current_card[0] == "B":
        if team_B_list.count(current_card) > 0:
            team_B_list.remove(current_card)
            if len(team_B_list) < 7:
                the_game_was_terminated = True
                print(f'Team A - {len(team_A_list)}; Team B - {len(team_B_list)}')
                print("Game was terminated")

if the_game_was_terminated == False:
    print(f'Team A - {len(team_A_list)}; Team B - {len(team_B_list)}')