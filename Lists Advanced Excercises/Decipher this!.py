list_of_decripted_words = (str(input())).split()
print_result = ""

for index in range(0, len(list_of_decripted_words)):
    current_decrypted_word = (list_of_decripted_words[index])
    current_decrypted_word_list = []
    for letter in current_decrypted_word:
        current_decrypted_word_list.append(letter)
    first_digit = current_decrypted_word_list.pop(0)
    second_digit = current_decrypted_word_list.pop(0)
    digits = first_digit + "" + second_digit
    if current_decrypted_word_list[0] == "1" or current_decrypted_word_list[0] == "2" or  current_decrypted_word_list[0] == "3" or current_decrypted_word_list[0] == "4" or current_decrypted_word_list[0] == "5" or current_decrypted_word_list[0] == "6" or current_decrypted_word_list[0] == "7" or current_decrypted_word_list[0] == "8" or current_decrypted_word_list[0] == "9" or current_decrypted_word_list[0] == "0":
        third_digit = current_decrypted_word_list.pop(0)
        digits += third_digit

    first_letter = chr(int(digits))
    if len(current_decrypted_word_list) > 1:
        second_letter = current_decrypted_word_list.pop(0)
        last_letter = current_decrypted_word_list.pop()
        current_decrypted_word_list.insert(0, last_letter)
        current_decrypted_word_list.append(second_letter)
    current_decrypted_word_list.insert(0, first_letter)

    print_result+= ("".join(current_decrypted_word_list) + " ")

print(print_result)

