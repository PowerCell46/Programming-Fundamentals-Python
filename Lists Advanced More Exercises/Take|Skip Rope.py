input_string = str(input())
numbers_list = []
non_numbers_list = []

for i in input_string:
    if 47 < ord(i) < 58:
        numbers_list.append(i)
    else:
        non_numbers_list.append(i)

take_list = [] # evens
skip_list = [] # odds

for i in range(0, len(numbers_list)):
    if i % 2 == 0:
        take_list.append(int(numbers_list[i]))
    else:
        skip_list.append(int(numbers_list[i]))


result_string = ""
counter = 0
index = 0
xedni = -1

for takeNum in take_list:
    while counter < takeNum and index < len(non_numbers_list):
        result_string += non_numbers_list[index]
        index += 1
        counter += 1
    counter = 0
    xedni += 1
    skipNum = skip_list[xedni]
    while counter < skipNum and index < len(non_numbers_list):
        index += 1
        counter += 1
    counter = 0

print(result_string)
