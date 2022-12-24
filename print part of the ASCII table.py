start = int(input())
end = int(input()) + 1
result = []

for index in range(start, end):
    current_character = chr(index)
    result.append(current_character)

print(*result, sep=" ")