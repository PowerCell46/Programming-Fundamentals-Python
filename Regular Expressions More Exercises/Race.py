import re

list_of_participants = input().split(", ")
race_dict = {}

while True:
    current_input = input()
    if current_input == "end of race":
        break
    current_name = "".join(re.findall("[A-Z|a-z]", current_input))
    current_km = sum([int(num) for num in re.findall("[0-9]", current_input)])
    if current_name in list_of_participants:
        if current_name not in race_dict.keys():
            race_dict[current_name] = 0
        race_dict[current_name] += current_km

race_dict = sorted(race_dict.items(), key=lambda x: -x[1])
for index in range(len(race_dict)):
    if index == 0:
        print(f'1st place: {race_dict[index][0]}')
    elif index == 1:
        print(f'2nd place: {race_dict[index][0]}')
    elif index == 2:
        print(f'3rd place: {race_dict[index][0]}')
        
