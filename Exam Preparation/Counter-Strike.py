initial_energy = int(input())

won_battles = 0

while True:
    distance_of_an_enemy = input()
    if distance_of_an_enemy == "End of battle":
        print(f'Won battles: {won_battles}. Energy left: {initial_energy}')
        break
    distance_of_an_enemy = int(distance_of_an_enemy)
    if initial_energy - distance_of_an_enemy >= 0:
        initial_energy -= distance_of_an_enemy
        won_battles += 1
        if won_battles % 3 == 0:
            initial_energy += won_battles
    else:
        print(f'Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy')
        break
