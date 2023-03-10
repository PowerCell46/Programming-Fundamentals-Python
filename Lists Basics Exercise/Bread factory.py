energy = 100
coins = 100
event_list = (str(input())).split("|")
you_have_completed_all_orders = True

for index in range(0, len(event_list)):
    current_input = (event_list[index]).split("-")
    current_event = current_input[0]
    current_number = int(current_input[1])

    if current_event == "rest":
        energy += current_number
        if energy > 100:
            leftout_energy = energy - 100
            energy = 100
            print(f'You gained {current_number - leftout_energy} energy.')
        else:
            print(f'You gained {current_number} energy.')
        print(f'Current energy: {energy}.')

    elif current_event == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += current_number
            print(f'You earned {current_number} coins.')
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins - current_number >= 0:
            coins -= current_number
            print(f'You bought {current_event}.')
        else:
            print(f'Closed! Cannot afford {current_event}.')
            you_have_completed_all_orders = False
            break

if you_have_completed_all_orders == True:
    print("Day completed!")
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')