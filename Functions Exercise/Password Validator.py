input_password = str(input())
counter = 0
numbers_counter = 0
the_pass_is_correct = True
first_time = True

for i in range(0, len(input_password)):
    current_digit = input_password[i]
    counter += 1
    if ord(current_digit) >= 48 and ord(current_digit) <= 57 or ord(current_digit) > 64 and ord(current_digit) < 91 or ord(current_digit) > 96 and ord(current_digit) < 123:
        if ord(current_digit) >= 48 and ord(current_digit) <= 57:
            numbers_counter += 1
    else:
        if first_time == True:
            print("Password must consist only of letters and digits")
            the_pass_is_correct = False
        first_time = False
if counter < 6 or counter > 10:
    print("Password must be between 6 and 10 characters")
    the_pass_is_correct = False

if numbers_counter < 2:
    print("Password must have at least 2 digits")
    the_pass_is_correct = False

if the_pass_is_correct == True:
    print("Password is valid")
