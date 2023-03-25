softuni_exam_results = {}
submissions_dictionary = {}

list_of_banned_people = []
while True:
    current_input = str(input())
    if current_input == "exam finished":
        break
    current_input = current_input.split("-")
    username = current_input[0]
    if current_input[1] == "banned":
        list_of_banned_people.append(username)
    else:
        language = current_input[1]
        points = int(current_input[2])

    if language not in softuni_exam_results.keys():
        softuni_exam_results[language] = {}

    if username not in list_of_banned_people:
        current_language_obj = softuni_exam_results[language]
        flag = False  # Флаг, с който проверяваме дали юзърнеймът го има в езика
        for rotating_username in current_language_obj:
            if username == rotating_username:
                flag = True
                if softuni_exam_results[language][username] < points: # Ако старите точки са по-малко от новите, сетни новите
                    softuni_exam_results[language][username] = points
                    break
        if flag == False:
            softuni_exam_results[language][username] = points
        if language not in submissions_dictionary.keys():
            submissions_dictionary[language] = 1
        else:
            previous_value = submissions_dictionary[language]
            submissions_dictionary[language] = (previous_value + 1)

print('Results:')
for language, obj in softuni_exam_results.items():
    for username in obj:
        if username not in list_of_banned_people:
            print(f'{username} | {softuni_exam_results[language][username]}')

print("Submissions:")
for language, submissions in submissions_dictionary.items():
    print(f'{language} - {submissions}')
    
