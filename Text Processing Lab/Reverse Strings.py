while True:
    current_word = str(input())
    if current_word == "end":
        break
    word_list = [letter for letter in current_word]
    word_list.reverse()
    print(f'{current_word} = {"".join(word_list)}')
