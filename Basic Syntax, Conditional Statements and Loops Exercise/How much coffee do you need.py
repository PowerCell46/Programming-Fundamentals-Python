sum_of_coffees = 0
while True:
    current_command = str(input())
    if current_command == "END":
        break
    if current_command == "CODING":
        sum_of_coffees += 2
    elif current_command == "coding":
        sum_of_coffees += 1
    elif current_command == "dog":
        sum_of_coffees += 1
    elif current_command == "DOG":
        sum_of_coffees += 2
    elif current_command == "movie":
        sum_of_coffees += 1
    elif current_command == "MOVIE":
        sum_of_coffees += 2
    elif current_command == "CAT":
        sum_of_coffees += 2
    elif current_command == "cat":
        sum_of_coffees += 1
    else:
        continue


if sum_of_coffees > 5:
    print("You need extra sleep")
elif sum_of_coffees <= 5:
    print(sum_of_coffees)
