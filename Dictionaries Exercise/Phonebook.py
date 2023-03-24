phone_book = {}
number_of_checkers = None

while True:
    current_input = input().split("-")
    if len(current_input) < 2:
        number_of_checkers = current_input[0]
        break
    current_name = current_input[0]
    current_phone = current_input[1]
    phone_book[current_name] = current_phone

while int(number_of_checkers) > 0:
    number_of_checkers = int(number_of_checkers) - 1
    current_name = str(input())
    if current_name in phone_book.keys():
        print(f'{current_name} -> {phone_book[current_name]}')
    else:
        print(f'Contact {current_name} does not exist.')
