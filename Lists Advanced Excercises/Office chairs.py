numbers_of_rooms = int(input())
counter = 0
everything_is_ok = True
left_chairs = 0

while numbers_of_rooms > 0:
    numbers_of_rooms -= 1
    counter += 1
    current_room = (str(input())).split()
    current_chairs = len(current_room[0])
    current_visitors = int(current_room[1])
    if current_visitors > current_chairs:
        print(f'{current_visitors - current_chairs} more chairs needed in room {counter}')
        everything_is_ok = False
    elif current_chairs > current_visitors:
        left_chairs += current_chairs - current_visitors

if everything_is_ok:
    print(f'Game On, {left_chairs} free chairs left')
