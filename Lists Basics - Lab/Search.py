number_n = int(input())
word = str(input())
first_list = []

for i in range(0, number_n):
    current_string = str(input())
    first_list.append(current_string)

second_list = []

for index in range(0, len(first_list)):
    current_string = first_list[index]
    for i in range(0, len(current_string)):
        current_letter = current_string[i]
        if current_letter == word[0]:
            if current_string[i + 1] == word[1]:
                if current_string[i + 2] == word[2]:
                    second_list.append(current_string)
                    break

print(first_list)
print(second_list)