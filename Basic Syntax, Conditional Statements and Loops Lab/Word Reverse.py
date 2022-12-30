input_word = str(input())
new_word = ""
for index in range((len(input_word) -1), -1, -1):
    current_letter = input_word[index]
    new_word += current_letter

print(new_word)
