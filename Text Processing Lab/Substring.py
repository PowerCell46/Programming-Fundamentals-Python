pattern = str(input())
string = str(input())

while pattern in string:
    string = string.replace(pattern, "")


print(string)
