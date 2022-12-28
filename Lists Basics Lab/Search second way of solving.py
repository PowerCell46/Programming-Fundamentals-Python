number_n = int(input())
word = str(input())
first_list = []

for i in range(0, number_n):
    current_str = str(input())
    first_list.append(current_str)

second_list = []

for index in range(0, len(first_list)):
    current_str = first_list[index]
    current_str = current_str.split()
    if current_str.count(word) > 0:
        second_list.append(first_list[index])

print(first_list)
print(second_list)