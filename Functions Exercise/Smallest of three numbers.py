list = []
first_num = int(input())
second_num = int(input())
third_num = int(input())
list.append(first_num)
list.append(second_num)
list.append(third_num)

def smallest_num(list):
    return min(list)

print(smallest_num(list))