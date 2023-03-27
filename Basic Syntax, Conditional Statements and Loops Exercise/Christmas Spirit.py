decoration_dictionary = {"Ornament set": {2: 5}, "Tree Skirt": {5: 3}, "Tree Garland": {3: 10}, "Tree Lights": {15: 17}}
quantity_of_decorations_for_each_shopping = int(input())
days_till_Christmas = int(input())
counter_days = 0

total_price = 0
total_points = 0

while days_till_Christmas > 0:
    counter_days += 1

    if counter_days % 11 == 0:
        quantity_of_decorations_for_each_shopping += 2

    if counter_days % 2 == 0:
        ornament_price = 2
        ornament_points = 5
        total_price += (ornament_price * quantity_of_decorations_for_each_shopping)
        total_points += ornament_points

    if counter_days % 3 == 0:
        tree_skirts_price = 5
        tree_skirts_points = 3
        tree_garlands_price = 3
        tree_garlands_points = 10
        total_price += ((tree_skirts_price * quantity_of_decorations_for_each_shopping) + (tree_garlands_price * quantity_of_decorations_for_each_shopping))
        total_points += tree_skirts_points + tree_garlands_points

    if counter_days % 5 == 0:
        tree_lights_price = 15
        tree_lights_points = 17
        total_price += (tree_lights_price * quantity_of_decorations_for_each_shopping)
        total_points += tree_lights_points
        if counter_days % 3 == 0:
            total_points += 30

    if counter_days % 10 == 0:
        total_points -= 20
        total_price += (5 + 3 + 15)
        if days_till_Christmas == 1:
            total_points -= 30
    days_till_Christmas -= 1

print(f'Total cost: {total_price}')
print(f'Total spirit: {total_points}')
