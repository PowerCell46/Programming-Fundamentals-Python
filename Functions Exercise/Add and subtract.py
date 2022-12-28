first_num = int(input())
second_num = int(input())
third_num = int(input())

def sum_numbers(first_num, second_num):
    return first_num + second_num

def subtract(third_num):
    return sum_numbers(first_num, second_num) - third_num

def add_and_subtract(first_num, second_num, third_num):
    print(subtract())

sum_numbers(first_num, second_num)
print(subtract(third_num))
