first_str, second_str = input().split(" ")
sum = 0

if len(first_str) == len(second_str):
    for i in range(0, len(first_str)):
        sum += (ord(first_str[i]) * ord(second_str[i]))

elif len(first_str) > len(second_str):
        for i in range(0, len(first_str)):
            if i >= len(second_str):
                sum += ord(first_str[i])
            else:
                sum += (ord(first_str[i]) * ord(second_str[i]))

elif len(first_str) < len(second_str):
        for i in range(0, len(second_str)):
            if i >= len(first_str):
                sum += ord(second_str[i])
            else:
                sum += (ord(first_str[i]) * ord(second_str[i]))

print(sum)
