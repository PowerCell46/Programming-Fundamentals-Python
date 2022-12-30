divisor = int(input())
boundary = int(input()) + 1

while True:
    boundary -= 1
    if boundary == 0:
        break
    if boundary % divisor == 0:
        print(boundary)
        break
