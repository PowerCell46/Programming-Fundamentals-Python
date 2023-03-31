import re

text_string = str(input())
pattern = r'(@|#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'

result = re.findall(pattern, text_string)

print_list = []
number_of_word_pairs = 0

for separator, text1, text2 in result:
    number_of_word_pairs += 1
    text1 = [letter for letter in text1]
    text1.reverse()
    text1 = "".join(text1)
    if text1 == text2:
        text1 = [letter for letter in text1]
        text1.reverse()
        text1 = "".join(text1)
        print_list.append(text1 + " <=> " + text2)

if number_of_word_pairs > 0:
    print(f'{number_of_word_pairs} word pairs found!')
else:
    print(f'No word pairs found!')

if len(print_list) > 0:
    print(f'The mirror words are:')
    print(f'{", ".join(print_list)}')
else:
    print('No mirror words!')
