number_of_synonyms = int(input()) * 2


synonyms_dictionary = {}

while number_of_synonyms > 0:
    number_of_synonyms -= 1
    current_word = str(input())
    if current_word in synonyms_dictionary.keys():
        previous_synonyms = synonyms_dictionary[current_word]
    else:
        previous_synonyms = []
    number_of_synonyms -= 1
    current_synonym = str(input())
    previous_synonyms.append(current_synonym)
    synonyms_dictionary[current_word] = previous_synonyms

for key, value in synonyms_dictionary.items():
    print(f'{key} - {", ".join(value)}')
