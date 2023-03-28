list_of_numbers = input().split(", ")
list_of_numbers = [int(num) for num in list_of_numbers]
minimum_value = int(input())
bigger_values = [num for num in list_of_numbers if num > minimum_value]
bigger_values.sort()
bigger_values.reverse()
flag = True

for index in range(0, len(list_of_numbers)):
    number = list_of_numbers[index]
    if number < minimum_value:
        needed_value = minimum_value - number
        for i in range(0, len(bigger_values)):
            num = bigger_values[i]
            if num - needed_value >= minimum_value:
                search_index = list_of_numbers.index(num)
                list_of_numbers[search_index] = num - needed_value
                bigger_values[i] = num - needed_value
                number += needed_value
                break
            else:
                res = num - minimum_value
                if res > 0:
                    search_index = list_of_numbers.index(num)

                    if res + number > minimum_value:
                        left = res + number - minimum_value
                        list_of_numbers[search_index] = minimum_value + left
                        bigger_values[i] = minimum_value + left
                        number = minimum_value
                    else:
                        list_of_numbers[search_index] = minimum_value
                        bigger_values[i] = minimum_value
                        number += res

        if number == minimum_value:
            list_of_numbers[index] = minimum_value
            bigger_values.sort()
            bigger_values.reverse()
        else:
            print("No equal distribution possible")
            flag = False
            break

if flag:
    print(list_of_numbers)
