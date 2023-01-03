input_number = int(input())
the_number_is_prime = True

for index in range(2, input_number):
    current_divider = index
    if input_number % current_divider == 0:
        the_number_is_prime = False
        break
    else:
        the_number_is_prime = True

if the_number_is_prime == True:
    print("True")
else:
    print("False")
