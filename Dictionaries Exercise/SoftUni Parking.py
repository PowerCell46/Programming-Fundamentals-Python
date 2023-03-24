number_of_lines = int(input())

parking_lot = {}

while number_of_lines > 0:
    number_of_lines -= 1
    current_input = str(input()).split(" ")
    if current_input[0] == "register":
        username = current_input[1]
        licence_place = current_input[2]
        if username in parking_lot.keys():
            print(f'ERROR: already registered with plate number {parking_lot[username]}')
        else:
            parking_lot[username] = licence_place
            print(f'{username} registered {licence_place} successfully')

    elif current_input[0] == "unregister":
        username = current_input[1]
        if username in parking_lot.keys():
            del parking_lot[username]
            print(f'{username} unregistered successfully')
        else:
            print(f'ERROR: user {username} not found')

for key, value in parking_lot.items():
    print(f'{key} => {value}')
    
