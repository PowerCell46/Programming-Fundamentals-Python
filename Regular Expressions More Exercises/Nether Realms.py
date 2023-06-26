import re

working_strings = re.split(r"\s*,\s*", input())
demon_book = {}

for working_string in working_strings:
    current_health = 0
    for char in working_string:
        if not char.isdigit() and char != "+" and char != "-" and char != "*" and char != "/" and char != ".":
            current_health += ord(char)

    current_numbers = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", working_string)
    current_damage = 0
    for num in current_numbers:
        if "-" in num or "+" in num:
            num = [el for el in num]
            if num[0] == "+":
                num.pop(0)
                current_damage += float("".join(num))
            else:
                num.pop(0)
                current_damage -= float("".join(num))
        else:
            current_damage += float(num)

    for el in working_string:
        if el == "*":
            current_damage *= 2
        elif el == "/":
            current_damage /= 2

    demon_book[working_string] = [current_health, current_damage]

demon_book = sorted(demon_book.items(), key=lambda x: x[0])
for tuple in demon_book:
    print(f'{tuple[0]} - {tuple[1][0]} health, {tuple[1][1]:.2f} damage')
