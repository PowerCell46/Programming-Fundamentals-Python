input_lines = int(input()) * 2

student_academy = {}
counter = 0

while input_lines > 0:
    input_lines -= 1
    current_student = str(input())
    input_lines -= 1
    current_grade = float(input())
    if current_student in student_academy.keys():
        counter += 1
        student_academy[current_student][current_grade] = "SoftUni" + str(counter)
    else:
        student_academy[current_student] = {}
        student_academy[current_student][current_grade] = "SoftUni"

final_student_academy = {}

for student, obj in student_academy.items():
    average_grade = 0
    for i in obj:
        average_grade += i
    average_grade = (average_grade / len(obj))
    final_student_academy[student] = average_grade

for student, average_grade in final_student_academy.items():
    if average_grade >= 4.5:
        print(f'{student} -> {average_grade:.2f}')
        
