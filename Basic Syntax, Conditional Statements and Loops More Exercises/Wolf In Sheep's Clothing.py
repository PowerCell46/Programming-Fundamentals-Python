task_array = str(input()).split(", ")
counter = 0

for index in range(len(task_array)- 1, -1, -1):
    current_animal = task_array[index]
    counter += 1
    if current_animal == "wolf" and counter != 1:
        print(f'Oi! Sheep number {counter -1}! You are about to be eaten by a wolf!')
        break
    if current_animal == "wolf" and counter == 1:
        print("Please go away and stop eating my sheep")
