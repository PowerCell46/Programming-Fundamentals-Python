storage_dictionary = {}

while True:
    current_input = str(input())
    if current_input == "statistics":
        break
    current_input = current_input.split(": ")
    current_product = current_input[0]
    current_quantity = int(current_input[1])
    if current_product in storage_dictionary.keys():
        previous_quantity = storage_dictionary[current_product]
        storage_dictionary[current_product] = (previous_quantity + current_quantity)
    else:
        storage_dictionary[current_product] = current_quantity

print("Products in stock:")
for product in storage_dictionary.keys():
    print(f'- {product}: {storage_dictionary[product]}')
print(f'Total Products: {len(storage_dictionary.keys())}')
total_products = [storage_dictionary[x] for x in storage_dictionary.keys()]
print(f'Total Quantity: {sum(total_products)}')
