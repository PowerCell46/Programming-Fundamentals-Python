factorial_num = int(input())
divider = int(input())
result = 1
second_result = 1

for i in range(factorial_num, 0, -1):
    result *= i

for index in range(divider, 0, -1):
    second_result *= index
    
result /= second_result
print(f'{result:.2f}')
