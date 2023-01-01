list_of_numbers = (str(input())).split(", ")
positive_list = []
negative_list = []
even_list = []
odd_list = []

for i in range(0, len(list_of_numbers)):
    current_num = int(list_of_numbers[i])
    if current_num >= 0:
        positive_list.append(str(current_num))
    else:
        negative_list.append(str(current_num))
    if current_num % 2 == 0:
        even_list.append(str(current_num))
    else:
        odd_list.append(str(current_num))

print("Positive:", ", ".join(positive_list) )
print("Negative:", ", ".join(negative_list) )
print("Even:", ", ".join(even_list) )
print("Odd:", ", ".join(odd_list) )
