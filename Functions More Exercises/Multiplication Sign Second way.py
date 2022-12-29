first_num = int(input())
second_num = int(input())
third_num = int(input())

if first_num < 0 and second_num < 0 and third_num < 0:
    print("negative")
elif first_num < 0 and second_num > 0 and third_num < 0:
    print("positive")
elif first_num < 0 and second_num > 0 and third_num > 0:
    print("negative")
elif first_num < 0 and second_num < 0 and third_num > 0:
    print("positive")
elif second_num < 0 and first_num > 0 and third_num < 0:
    print("positive")
elif second_num < 0 and first_num > 0 and third_num > 0:
    print("negative")
elif second_num < 0 and first_num > 0 and third_num > 0:
    print("positive")
elif third_num < 0 and first_num > 0 and second_num < 0:
    print("positive")
elif first_num > 0 and second_num > 0 and third_num > 0:
    print("positive")
elif first_num > 0 and second_num > 0 and third_num < 0:
    print("negative")
elif first_num == 0 or second_num == 0 or third_num == 0:
    print("zero")
