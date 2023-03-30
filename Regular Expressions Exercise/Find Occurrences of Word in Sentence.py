input_text = str(input()).split(" ")
searched_word = str(input())
counter = 0

for word in input_text:
    if word.lower() == searched_word.lower() or word.lower() == searched_word.lower() + "?" or word.lower() == searched_word.lower() + "." or word.lower() == searched_word.lower() + "," or word.lower() == searched_word.lower() + "!" or word.lower() == searched_word.lower() + ";" or word.lower() == searched_word.lower() + ":":
        counter += 1

print(counter)
