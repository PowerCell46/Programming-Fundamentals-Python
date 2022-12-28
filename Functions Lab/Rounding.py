numbers_list = (str(input())).split()
print_list = []

def rounding(current_num):
    current_num = round(current_num)
    print_list.append(current_num)

for i  in range(0, len(numbers_list)):
    current_num = float(numbers_list[i])
    rounding(current_num)

print(print_list)