max_value = int(input())
first_cycle = ""
list = []
for index in range(0, max_value):
    first_cycle += "*"
    list.append("*")
    print(first_cycle)
for xedni in range(max_value - 1, 0, -1):
    list.pop()
    print(*list, sep="")
