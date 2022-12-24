capacity = 255
number_of_lines = int(input())
collected_water = 0
while True:
    number_of_lines -= 1
    if number_of_lines == -1:
        print(collected_water)
        break
    current_water = int(input())
    collected_water += current_water
    if collected_water > capacity:
        print("Insufficient capacity!")
        collected_water -= current_water
        continue