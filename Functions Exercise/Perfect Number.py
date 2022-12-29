input_number = int(input())
sum_of_divisors = 0

for i in range((input_number -1), 0, -1):
    if input_number % i == 0:
        sum_of_divisors += i

if sum_of_divisors == input_number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
