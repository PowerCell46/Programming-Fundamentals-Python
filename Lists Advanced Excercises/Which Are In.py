searched_word = (str(input())).split(", ")
word_list = (str(input())).split(", ")
letters_word_list = []
found_words_list = []

for i in range(0, len(word_list)):
    current_word = word_list[i]
    for index in range(0, len(current_word)):
        letters_word_list.append(current_word[index])

index1 = 0
index2 = 0
while True:
    if index1 == len(searched_word):
        break
    current_searched_word = searched_word[index1]
    current_letter = letters_word_list[index2]
    if current_searched_word[0] == current_letter:
        if current_searched_word[1] == letters_word_list[index2 + 1]:
            if current_searched_word[2] == letters_word_list[index2 + 2]:
                found_words_list.append(current_searched_word)
                index2 = 0
                index1 += 1
    index2 += 1
    if index2 == len(letters_word_list):
        index1 += 1
        index2 = 0
print(found_words_list)
