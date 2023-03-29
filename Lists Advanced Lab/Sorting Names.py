names = (str(input())).split(", ")
result = sorted(names, key= lambda item: (-len(item), item))
print(result)
