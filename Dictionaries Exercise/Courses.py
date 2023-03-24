course_dictionary = {}

while True:
    current_input = str(input())
    if current_input == "end":
        break
    current_input = current_input.split(" : ")
    current_course = current_input[0]
    current_student = current_input[1]
    if current_course in course_dictionary.keys():
        course_dictionary[current_course][current_student] = "SoftUni"
    else:
        course_dictionary[current_course] = {}
        course_dictionary[current_course][current_student] = "SoftUni"

for course, obj in course_dictionary.items():
    print(f'{course}: {len(obj)}')
    for i in obj:
        print(f'-- {i}')
