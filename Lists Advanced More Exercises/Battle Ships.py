number_of_rows = int(input())
sea_field = []
destroyed_ships = 0

while number_of_rows > 0:
    number_of_rows -= 1
    current_row = str(input()).split(" ")
    current_row = [int(num) for num in current_row]
    sea_field.append(current_row)

attacks_list = str(input()).split(" ")

for attack in attacks_list:
    row, column = attack.split("-")
    current_row = sea_field[int(row)]
    current_ship = current_row[int(column)]
    if current_ship > 0:
        current_ship -= 1
        if current_ship == 0:
            destroyed_ships += 1
    current_row[int(column)] = current_ship
    sea_field[int(row)] = current_row

print(destroyed_ships)
