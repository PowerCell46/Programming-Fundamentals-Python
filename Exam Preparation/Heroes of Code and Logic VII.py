number_of_heroes = int(input())
hero_dictionary = {}

while number_of_heroes > 0:
    number_of_heroes -= 1
    current_input = str(input()).split(" ")
    hero_name = current_input[0]
    hp = int(current_input[1])
    mana_points = int(current_input[2])
    hero_dictionary[hero_name] = {}
    hero_dictionary[hero_name][hp] = mana_points

while True:
    current_input = str(input())
    if current_input == "End":
        break
    current_input = current_input.split(" - ")

    if current_input[0] == "CastSpell":
        hero_name = current_input[1]
        mp_needed = int(current_input[2])
        spell_name = (current_input[3])
        stored_mp = list(hero_dictionary[hero_name].values())
        stored_mp = stored_mp[0]
        if mp_needed <= stored_mp:
            stored_hp = list(hero_dictionary[hero_name].keys())
            hero_dictionary[hero_name][stored_hp[0]] = (stored_mp - mp_needed)
            print(f'{hero_name} has successfully cast {spell_name} and now has {stored_mp - mp_needed} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')

    elif current_input[0] == "TakeDamage":
        hero_name = current_input[1]
        damage = int(current_input[2])
        attacker = current_input[3]
        stored_hp = list(hero_dictionary[hero_name].keys())
        stored_hp = stored_hp[0]
        new_hp = stored_hp - damage
        if new_hp > 0:
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {new_hp} HP left!')
            stored_mp = hero_dictionary[hero_name][stored_hp]
            del hero_dictionary[hero_name][stored_hp]
            hero_dictionary[hero_name][new_hp] = stored_mp
        else:
            del hero_dictionary[hero_name]
            print(f'{hero_name} has been killed by {attacker}!')

    elif current_input[0] == "Recharge":
        hero_name = current_input[1]
        amount = int(current_input[2])
        stored_mp = list(hero_dictionary[hero_name].values())
        stored_mp = stored_mp[0]
        if stored_mp + amount <= 200:
            stored_hp = list(hero_dictionary[hero_name].keys())
            stored_hp = stored_hp[0]
            hero_dictionary[hero_name][stored_hp] = (stored_mp + amount)
            print(f'{hero_name} recharged for {amount} MP!')
        else:
            stored_hp = list(hero_dictionary[hero_name].keys())
            stored_hp = stored_hp[0]
            hero_dictionary[hero_name][stored_hp] = 200
            print(f'{hero_name} recharged for {(amount - (stored_mp + amount - 200))} MP!')

    elif current_input[0] == "Heal":
        hero_name = current_input[1]
        amount = int(current_input[2])
        stored_hp = list(hero_dictionary[hero_name].keys())
        stored_hp = stored_hp[0]
        if stored_hp + amount <= 100:
            stored_mp = list(hero_dictionary[hero_name].values())
            stored_mp = stored_mp[0]
            del hero_dictionary[hero_name][stored_hp]
            hero_dictionary[hero_name][(stored_hp + amount)] = stored_mp
            print(f'{hero_name} healed for {amount} HP!')
        else:
            stored_mp = list(hero_dictionary[hero_name].values())
            stored_mp = stored_mp[0]
            del hero_dictionary[hero_name][stored_hp]
            hero_dictionary[hero_name][100] = stored_mp
            print(f'{hero_name} healed for {amount - (stored_hp + amount - 100)} HP!')

for key, value in hero_dictionary.items():
    print(key)
    for hp, mp in value.items():
        print(f'    HP: {hp}')
        print(f'    MP: {mp}')
