contests = {}

contests_submissions = {}
while True:
    current_input = str(input())
    if current_input == "end of contests":
        break
    current_input = current_input.split(":")
    contests[current_input[0]] = current_input[1]
    contests_submissions[current_input[0]] = {}

top_result = ""
top_result_1 = 0

while True:
    current_input = str(input())
    if current_input == "end of submissions":
        break
    current_input = current_input.split("=>")
    if current_input[0] in contests.keys():
        if contests[current_input[0]] == current_input[1]:
            if current_input[2] not in contests_submissions[current_input[0]].keys():
                contests_submissions[current_input[0]][current_input[2]] = int(current_input[3])
                if int(current_input[3]) > top_result_1:
                    top_result = current_input[2]
                    top_result_1 = int(current_input[3])
            else:
                previous_value = contests_submissions[current_input[0]][current_input[2]]
                if previous_value < int(current_input[3]):
                    contests_submissions[current_input[0]][current_input[2]] = int(current_input[3])
                    if int(current_input[3]) > top_result_1:
                        top_result = current_input[2]
                        top_result_1 = int(current_input[3])


best_candidate_points = 0
list_of_names = []
final_dict = {}

for key, value in contests_submissions.items():
    current_names = (value.keys())
    for name in current_names:
        list_of_names.append(name)
        if name == top_result:
            best_candidate_points += contests_submissions[key][name]
        if name not in final_dict.keys():
            final_dict[name] = {}
            final_dict[name][contests_submissions[key][name]] = key
        else:
            final_dict[name][contests_submissions[key][name]] = key

print(f'Best candidate is {top_result} with total {best_candidate_points} points.')
print("Ranking: ")
list_of_names = set(list_of_names)
list_of_names = list(list_of_names)
list_of_names.sort()

for name in list_of_names:
    current_persons_points_list = list(final_dict[name].keys())
    current_persons_points_list.sort()
    current_persons_points_list.reverse()
    print(name)
    while len(current_persons_points_list) > 0:
        current_points = current_persons_points_list[0]
        print(f'#  {final_dict[name][current_points]} -> {current_points}')
        current_persons_points_list.pop(0)
