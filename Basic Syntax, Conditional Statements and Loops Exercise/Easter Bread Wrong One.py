budget = float(input())
price_for_a_kg_of_flour = float(input())
price_for_a_pack_of_eggs = 75 * (price_for_a_kg_of_flour / 100)
price_for_a_liter_of_milk = price_for_a_kg_of_flour + ((price_for_a_kg_of_flour / 100) * 25)
current_quantity_of_milk = 0
number_of_loaves = 0
number_of_eggs = 0

while True:
    price_for_a_loaf_of_bread = price_for_a_kg_of_flour + price_for_a_pack_of_eggs + (price_for_a_liter_of_milk / 4)

    if budget - price_for_a_loaf_of_bread < 0:
        break
    budget -= price_for_a_loaf_of_bread

    current_quantity_of_milk -= 250
    number_of_loaves += 1
    number_of_eggs += 3
    if number_of_loaves % 3 == 0:
        number_of_eggs -= (number_of_loaves - 2)

print(f'You made {number_of_loaves} loaves of Easter bread! Now you have {number_of_eggs} eggs and {budget:.2f}BGN left.')

