list_of_words = (str(input())).split()

print_list = []

for i in range(0, len(list_of_words)):
    current_word = list_of_words[i]
    if len(current_word) % 2 == 0:
        print_list.append(current_word)

print("\n".join(print_list))