import re
total_income = 0
while True:
    current_input = input()
    if current_input == "end of shift":
        break
    res = (re.search("\%([A-Z]{1}[a-z]{1,})\%([^|$\%.]{0,}?)\<([\w]{1,})\>([^|$\%.]{0,}?)\|([0-9]{1,})\|([^|$\%.]{0,}?)(\d{1,}\.?\d{0,}?)\$", current_input))
    if bool(res):
        current_name = res.group(1)
        current_product = res.group(3)
        current_quantity = int(res.group(5))
        current_price = float(res.group(7)) * current_quantity
        total_income += current_price
        print(f'{current_name}: {current_product} - {current_price:.2f}')

print(f'Total income: {total_income:.2f}')
