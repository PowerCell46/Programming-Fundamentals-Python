list_of_nums = input().split()
rotation = int(input())
index = 0
list_of_killed_people = []

while len(list_of_nums) > 0:
    index += (rotation - 1)
    while index >= len(list_of_nums):
        index -= len(list_of_nums)
    list_of_killed_people.append((list_of_nums.pop(index)))

print(f'[{",".join(list_of_killed_people)}]')
