students_dictionary = {}

while True:
    current_input = (input())
    current_input = ([*current_input])
    if current_input.count(":") == 0:
        current_input = ("".join(current_input).split("_"))
        current_input = " ".join(current_input)
        for student in students_dictionary.keys():
            current_student_course = students_dictionary[student]
            course = current_student_course.keys()
            for course1 in course:
                if course1 == current_input:
                    print(f'{student} - {students_dictionary[student][course1]}')
        break

    current_input = "".join(current_input).split(":")
    students_dictionary[current_input[0]] = {}
    students_dictionary[current_input[0]][current_input[2]] = int(current_input[1])
