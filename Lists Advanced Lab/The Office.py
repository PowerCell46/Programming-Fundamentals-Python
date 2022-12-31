employees_happiness_list = (str(input())).split()
factor = int(input())
sum_of_happiness = 0

for i in range(0, len(employees_happiness_list)):
    current_person = int(employees_happiness_list[i])
    sum_of_happiness += current_person * factor

average_happiness = sum_of_happiness / len(employees_happiness_list)
happiness_counter = 0
for i in range(0, len(employees_happiness_list)):
    current_person_happiness = int(employees_happiness_list[i]) * factor
    if current_person_happiness >= average_happiness:
        happiness_counter += 1

if happiness_counter >= len(employees_happiness_list) / 2:
    print(f'Score: {happiness_counter}/{len(employees_happiness_list)}. Employees are happy!')
else:
    print(f'Score: {happiness_counter}/{len(employees_happiness_list)}. Employees are not happy!')
