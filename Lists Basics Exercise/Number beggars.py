string_of_integers = str(input())
list_of_integers = string_of_integers.split(", ")

count_of_beggars = int(input())
list_of_beggars = []
length_of_the_beggars = count_of_beggars

while count_of_beggars > 0:
    list_of_beggars.append(0)
    count_of_beggars -= 1

for i in range(0, len(list_of_integers)):
    current_integer = int(list_of_integers[i])
    if i >= len(list_of_beggars):
        while i >= len(list_of_beggars):
            i -= len(list_of_beggars)

    current_beggar = list_of_beggars[i]
    current_beggar += current_integer
    list_of_beggars[i] = current_beggar

print(list_of_beggars)

