input_line = str(input()).split(" ")

occurrences_dictionary = {}

for word in input_line:
    word = word.lower()
    if word in occurrences_dictionary.keys():
        occurrences_dictionary[word] += 1
    else:
        occurrences_dictionary[word] = 1

print_string = ""
for key, value in occurrences_dictionary.items():
    if value % 2 != 0:
        print_string += key + " "

print(print_string)
