input_strings = str(input()).split(" ")
new_strings = ""
for string in input_strings:
    new_strings += string * len(string)
print(new_strings)
