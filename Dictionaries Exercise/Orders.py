products_dictionary = {}

while True:
    current_input = str(input())
    if current_input == "buy":
        break
    current_input = current_input.split(" ")
    current_product = current_input[0]
    current_price = float(current_input[1])
    current_quantity = int(current_input[2])

    if current_product in products_dictionary.keys():
        current_dictionary = products_dictionary[current_product]
        for i in current_dictionary.values():
            current_quantity += i
        products_dictionary[current_product].clear()
        products_dictionary[current_product][current_price] = current_quantity

    else:
        products_dictionary[current_product] = {}
        products_dictionary[current_product][current_price] = current_quantity

for key, dictionary in products_dictionary.items():
    current_result = 1
    for i in dictionary.keys():
        current_result *= float(i)
    for i in dictionary.values():
        current_result *= int(i)
    print(f'{key} -> {current_result:.2f}')
