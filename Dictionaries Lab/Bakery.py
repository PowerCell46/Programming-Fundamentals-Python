input_line = str(input()).split(" ")

even = [input_line[x] for x in range(0, len(input_line), 2)]
odd = [int(input_line[x]) for x in range(1, len(input_line), 2)]

bakery_dictionary = dict(zip(even, odd))
print(bakery_dictionary)
