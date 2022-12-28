input_string = str(input())
counter_n = int(input())

def repeat_string(input_string, counter_n):
    result = ""
    while counter_n != 0:
        result += input_string
        counter_n -= 1
    print(result)

repeat_string(input_string, counter_n)