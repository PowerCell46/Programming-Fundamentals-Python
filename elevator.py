number_of_people = int(input())
number_of_people_in_the_elevator = int(input())
counter = 0
while number_of_people > 0:
    number_of_people -= number_of_people_in_the_elevator
    counter += 1

print(counter)