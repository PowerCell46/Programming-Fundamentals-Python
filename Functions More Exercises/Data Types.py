type_of_data = str(input())

def result(type_of_data):
    if type_of_data == "int":
        number = int(input())
        number *= 2
        print(number)
    elif type_of_data == "real":
        number = float(input())
        number *= 1.5
        print(f'{number:.2f}')
    elif type_of_data == "string":
        string = str(input())
        print(f'${string}$')

result(type_of_data)
