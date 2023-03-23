character_list = input().split(", ")
character_dictionary = {}

for char in character_list:
    character_dictionary[char] = ord(char)

print(character_dictionary)
