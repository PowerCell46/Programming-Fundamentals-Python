import re
number_of_messages = int(input())
attacked_planets = []
destroyed_planets = []

for _ in range(number_of_messages):
    current_input = input()
    number_of_letters = 0
    for char in current_input:
        if char.lower() == "s" or char.lower() == "t" or char.lower() == "a" or char.lower() == "r":
            number_of_letters += 1
    working_string = ""
    for char in current_input:
        working_string += chr(ord(char) - number_of_letters)

    valid_input = True
    current_data = re.findall("^([^@\-!:>]{0,}?)\@([A-Z|a-z]+)([^@\-!:>]{0,}?)\:(([0-9]+))([^@\-!:>]{0,}?)\!(([A|D]))\!([^@\-!:>]{0,}?)\-\>(([0-9]+))([^@\-!:>]{0,}?)", working_string)
    if len(current_data) > 0:
        current_planet = current_data[0][1]
        current_population = int(current_data[0][3])
        current_attack = current_data[0][6]
        current_soldier_count = int(current_data[0][9])
        if current_attack == "A":
            attacked_planets.append(current_planet)
        elif current_attack == "D":
            destroyed_planets.append(current_planet)

attacked_planets = sorted(attacked_planets, key=lambda x: x)
destroyed_planets = sorted(destroyed_planets, key=lambda x: x)

print(f'Attacked planets: {len(attacked_planets)}')
for planet in attacked_planets:
    print(f'-> {planet}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in destroyed_planets:
    print(f'-> {planet}')
