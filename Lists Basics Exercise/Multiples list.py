factor = int(input())
count = int(input())
print_array = []

for i in range(0, count):
    multiplier = i + 1
    current_num = factor * multiplier
    print_array.append(current_num)

print(print_array)