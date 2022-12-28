import math

operator = str(input())
first_num = int(input())
second_num = int(input())

def calculations(operator, first_num, second_num):
    if operator == "multiply":
        print(math.trunc(first_num * second_num))
    elif operator == "divide":
        print(math.trunc(first_num / second_num))
    elif operator == "add":
        print(first_num + second_num)
    elif operator == "subtract":
        print(first_num - second_num)

calculations(operator, first_num, second_num)