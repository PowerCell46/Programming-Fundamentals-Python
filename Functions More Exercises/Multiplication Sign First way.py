positives = 0
negatives = 0
zeros = 0


for i in range(0, 3):
    current_num = int(input())
    if current_num > 0:
        positives += 1
    elif current_num == 0:
        zeros += 1
    elif current_num < 0:
        negatives += 1

if zeros > 0:
    print("zero")
elif negatives == 1:
    print("negative")
elif negatives == 2:
    print("positive")
elif negatives == 3:
    print("negative")
else:
    print("positive")
