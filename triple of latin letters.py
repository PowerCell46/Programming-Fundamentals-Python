integer = int(input())

for index in range(97, 97 + integer):
    first_letter = chr(index)
    for i in range(97, 97 + integer):
        second_letter = chr(i)
        for xedni in range(97, 97 + integer):
            third_letter = chr(xedni)
            print(f'{first_letter}{second_letter}{third_letter}')