numbers_list = (str(input())).split()
searched_word = str(input())
reversed_list = []

for i in range(0, len(numbers_list)):
    current_word = numbers_list[i]
    if current_word == current_word[::-1]:
        reversed_list.append(numbers_list[i])

print(reversed_list)
print(f'Found palindrome {numbers_list.count(searched_word)} times')
