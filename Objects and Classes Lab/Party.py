list = []

while (True):
    current_input = str(input())
    if current_input == "End":
        break
    list.append(current_input)

print(f'Going: {", ".join(list)}')
print(f'Total: {len(list)}')
