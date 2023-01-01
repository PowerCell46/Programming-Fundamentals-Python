software_version_list = (str(input())).split(".")
first_num = int(software_version_list[0])
second_num = int(software_version_list[1])
third_num = int(software_version_list[2])

if third_num < 9:
    third_num += 1

elif third_num == 9:
    second_num += 1
    third_num = 0


if second_num == 10:
    first_num += 1
    second_num = 0


if first_num == 9 and second_num == 9 and third_num == 9 or first_num == 10:
    print(f'9.9.9')
else:
    print(f'{first_num}.{second_num}.{third_num}')
