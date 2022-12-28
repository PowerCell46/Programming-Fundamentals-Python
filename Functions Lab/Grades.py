grade = float(input())

def grades(grade):
    if grade >= 2 and grade < 3:
        print("Fail")
    elif grade >= 3 and grade < 3.50:
        print("Poor")
    elif grade >= 3.50 and grade < 4.50:
        print("Good")
    elif grade >= 4.50 and grade < 5.50:
        print("Very Good")
    elif grade >= 5.50 and grade <= 6:
        print("Excellent")

grades(grade)