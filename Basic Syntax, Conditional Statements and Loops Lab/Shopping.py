budget = int(input())

while True:
    current_price = str(input())
    if current_price == "End":
        break
    else:
        current_price = int(current_price)
        budget -= current_price
        if budget < 0:
            print("You went in overdraft!")
            break
        
if budget >= 0:
    print("You bought everything needed.")
