input_list = (str(input())).split("|")
budget = float(input())

list_of_bought_things = []


for i in range(0, len(input_list)):
    current_input = (input_list[i]).split("->")
    current_type = current_input[0]
    current_price = float(current_input[1])

    if current_type == "Clothes":
        if current_price > 50 or current_price > budget:
            continue
        else:
            budget -= current_price
            list_of_bought_things.append(current_price)

    elif current_type == "Shoes":
        if current_price > 35 or current_price > budget:
            continue
        else:
            budget -= current_price
            list_of_bought_things.append(current_price)

    elif current_type == "Accessories":
        if current_price > 20.50 or current_price > budget:
            continue
        else:
            budget -= current_price
            list_of_bought_things.append(current_price)

new_prices_list = []
profit = 0

for i in range(0, len(list_of_bought_things)):
    current_bought_price = float(list_of_bought_things[i])
    new_price = current_bought_price + ((current_bought_price / 100) * 40)
    new_prices_list.append(f'{new_price:.2f}')
    profit += (new_price - current_bought_price)
    budget += new_price

print(" ".join(new_prices_list))
print(f'Profit: {profit:.2f}')

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

