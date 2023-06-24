judge = {}
total_points_dict = {}

while True:
    current_input = input()
    if current_input == "no more time":
        break
    current_input = current_input.split(" -> ")
    current_username = current_input[0]
    current_contest = current_input[1]
    current_points = int(current_input[2])

    flag = False
    if current_contest not in judge.keys():
        judge[current_contest] = {}
    if current_username not in judge[current_contest].keys():
        judge[current_contest][current_username] = current_points
        flag = True

    else:
        if current_points > judge[current_contest][current_username]:
            total_points_dict[current_username] -= judge[current_contest][current_username]
            judge[current_contest][current_username] = current_points
            flag = True

    if flag:
        if current_username not in total_points_dict.keys():
            total_points_dict[current_username] = 0
        total_points_dict[current_username] += current_points

for contest in judge.keys():
    current_contest_dict = sorted(judge[contest].items(), key=lambda x: (-x[1], x[0]))
    print(f'{contest}: {len(current_contest_dict)} participants')
    index = 1
    for tuple in current_contest_dict:
        print(f'{index}. {tuple[0]} <::> {tuple[1]}')
        index += 1


total_points_dict = sorted(total_points_dict.items(), key=lambda x: (-x[1], x[0]))
print(f'Individual standings:')
index = 1
for tuple in total_points_dict:
    print(f'{index}. {tuple[0]} -> {tuple[1]}')
    index += 1
