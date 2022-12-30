number_of_inputs = int(input())
the_number_is_even = True
while True:
    number_of_inputs -= 1
    if number_of_inputs == -1:
        break
    current_num = int(input())
    if current_num % 2 != 0:
        print(f'{current_num} is odd!')
        the_number_is_even = False
        break
if the_number_is_even == True:
    print("All numbers are even.")
