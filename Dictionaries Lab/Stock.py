input_stock = str(input()).split(" ")
even = [input_stock[x] for x in range(0, len(input_stock), 2)]
odd = [int(input_stock[x]) for x in range(1, len(input_stock), 2)]
my_stock_dictionary = dict(zip(even, odd))

searched_products = str(input()).split(" ")

for product in searched_products:
    if product in my_stock_dictionary.keys():
        print(f'We have {my_stock_dictionary[product]} of {product} left')
    else:
        print("Sorry, we don't have " + product)
