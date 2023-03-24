storage_dictionary = {}

while True:
    current_input = str(input())
    if current_input == "stop":
        break
    resource = current_input
    quantity = int(input())
    if resource in storage_dictionary.keys():
        previous_quantity = storage_dictionary[resource]
        storage_dictionary[resource] = (previous_quantity + quantity)
    else:
        storage_dictionary[resource] = quantity

for key,value in storage_dictionary.items():
    print(f'{key} -> {value}')
