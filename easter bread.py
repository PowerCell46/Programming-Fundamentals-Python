budget = float(input())
price_for_1kg_flour = float(input())
price_for_1pack_eggs = ((price_for_1kg_flour / 100) * 75)
price_for_1liter_milk =  price_for_1kg_flour + ((price_for_1kg_flour / 100) * 25)

milk_counter = 0
kozunak_counter = 0
colored_eggs = 0

while True:
    budget = budget - (price_for_1kg_flour + price_for_1pack_eggs)
    if milk_counter == 0:
        budget -= price_for_1liter_milk
        milk_counter = 4
    milk_counter -= 1

    if budget < 0:
        budget += (price_for_1kg_flour + price_for_1pack_eggs)
        if milk_counter == 3:
            budget += price_for_1liter_milk
        break
    kozunak_counter += 1
    colored_eggs += 3
    if kozunak_counter % 3 == 0:
        colored_eggs -= (kozunak_counter - 2)

print(f'You made {kozunak_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')