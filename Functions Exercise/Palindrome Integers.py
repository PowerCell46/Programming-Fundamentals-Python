list_of_numbers = (input()).split(", ")

for i in range(0, len(list_of_numbers)):
    current_num = list_of_numbers[i]
    if current_num == current_num[::-1]:
        print("True")
    else:
        print("False")
