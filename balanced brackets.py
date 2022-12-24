number_of_lines = int(input())
open_bracket = 0
closed_bracket = 0
terminate = False

for i in range(0, number_of_lines):
    current_symbol = str(input())

    if current_symbol == "(":
        open_bracket += 1
        if terminate == True:
            break
        terminate = True

    elif current_symbol == ")":
        closed_bracket += 1
        terminate = False


if closed_bracket == open_bracket and terminate == False:
    print("BALANCED")
else:
    print("UNBALANCED")