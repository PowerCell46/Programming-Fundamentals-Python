product = str(input())
quantity = int(input())

def orders(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2
    elif product == "water":
        price = 1
    result = price * quantity
    print(f'{result:.2f}')

orders(product, quantity)