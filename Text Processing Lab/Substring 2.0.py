pattern = str(input())
string = str(input())

while pattern in string:
    searched_index = string.index(pattern)
    string_list = [letter for letter in string]
    del string_list[searched_index: (searched_index + len(pattern))]
    string = "".join(string_list)

print(string)
