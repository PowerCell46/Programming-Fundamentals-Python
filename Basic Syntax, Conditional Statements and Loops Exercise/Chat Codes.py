number_of_massages = int(input())
while True:
    number_of_massages -= 1
    if number_of_massages == -1:
        break
    current_message = int(input())
    if current_message == 88:
        print("Hello")
    elif current_message == 86:
        print("How are you?")
    elif current_message < 88:
        print("GREAT!")
    elif current_message > 88:
        print("Bye.")
