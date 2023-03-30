input_string = str(input())

for i, letter in enumerate(input_string):
    if letter == ":":
        print(letter + input_string[i+1])
        
