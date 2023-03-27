numbers = input().split(" ")
list_of_numbers = [int(num) for num in numbers]

while True:
    current_input = input()
    if current_input == "end":
        break
    current_input = current_input.split(" ")

    if current_input[0] == "exchange":
        exchange_index = int(current_input[1])
        if len(list_of_numbers) > exchange_index >= 0:
            first_half = list_of_numbers[:exchange_index + 1]
            second_half = list_of_numbers[exchange_index + 1:]
            final_list = second_half + first_half
            list_of_numbers = final_list
        else:
            print('Invalid index')

    elif current_input[0] == "max":
        if current_input[1] == "even":
            list_of_evens_max = [number for number in list_of_numbers if number % 2 == 0]
            if len(list_of_evens_max) == 0:
                print("No matches")
            else:
                max_even = max(list_of_evens_max)
                if list_of_numbers.count(max_even) > 1:
                    copy_list = list_of_numbers[:]
                    while copy_list.count(max_even) > 1:
                        search_index = copy_list.index(max_even)
                        copy_list[search_index] = "-"
                    print(copy_list.index(max_even))
                else:
                    print(list_of_numbers.index(max_even))
        elif current_input[1] == "odd":
            list_of_odds_max = [number for number in list_of_numbers if number % 2 != 0]
            if len(list_of_odds_max) == 0:
                print("No matches")
            else:
                max_odd = max(list_of_odds_max)
                if list_of_numbers.count(max_odd) > 1:
                    copy_list = list_of_numbers[:]
                    while copy_list.count(max_odd) > 1:
                        search_index = copy_list.index(max_odd)
                        copy_list[search_index] = "+"
                    print(copy_list.index(max_odd))
                else:
                    print(list_of_numbers.index(max_odd))

    elif current_input[0] == "min":
        if current_input[1] == "even":
            list_of_evens_min = [number for number in list_of_numbers if number % 2 == 0]
            if len(list_of_evens_min) == 0:
                print("No matches")
            else:
                min_even = min(list_of_evens_min)
                if list_of_numbers.count(min_even) > 1:
                    copy_list = list_of_numbers[:]
                    while copy_list.count(min_even) > 1:
                        search_index = copy_list.index(min_even)
                        copy_list[search_index] = "*"
                    print(copy_list.index(min_even))
                else:
                    print(list_of_numbers.index(min_even))
        elif current_input[1] == "odd":
            list_of_odds_min = [number for number in list_of_numbers if number % 2 != 0]
            if len(list_of_odds_min) == 0:
                print('No matches')
            else:
                min_odd = min(list_of_odds_min)
                if list_of_numbers.count(min_odd) > 1:
                    copy_list = list_of_numbers[:]
                    while copy_list.count(min_odd) > 1:
                        search_index = copy_list.index(min_odd)
                        copy_list[search_index] = "/"
                    print(copy_list.index(min_odd))
                else:
                    print(list_of_numbers.index(min_odd))

    elif current_input[0] == "first":
        count = int(current_input[1])
        if count > len(list_of_numbers):
            print("Invalid count")
            continue
        count_list = []

        if current_input[2] == "even":
            even_numbers = [number for number in list_of_numbers if number % 2 == 0]
            if len(even_numbers) == 0:
                print("[]")
            else:
                for number in even_numbers:
                    count_list.append(number)
                    count -= 1
                    if count == 0:
                        break
                print(count_list)

        elif current_input[2] == "odd":
            odd_numbers = [number for number in list_of_numbers if number % 2 != 0]
            if len(odd_numbers) == 0:
                print("[]")
            else:
                for number in odd_numbers:
                    count_list.append(number)
                    count -= 1
                    if count == 0:
                        break
                print(count_list)

    elif current_input[0] == "last":
        count = int(current_input[1])
        if count > len(list_of_numbers):
            print("Invalid count")
            continue
        count_list_last = []

        if current_input[2] == "even":
            even_numbers = [number for number in list_of_numbers if number % 2 == 0]
            if len(even_numbers) == 0:
                print('[]')
            else:
                even_numbers.reverse()
                for number in even_numbers:
                    count_list_last.append(number)
                    count -= 1
                    if count == 0:
                        break
                count_list_last.reverse()
                print(count_list_last)

        elif current_input[2] == "odd":
            odd_numbers = [number for number in list_of_numbers if number % 2 != 0]
            odd_numbers.reverse()
            for number in odd_numbers:
                count_list_last.append(number)
                count -= 1
                if count == 0:
                    break
            count_list_last.reverse()
            print(count_list_last)

print(list_of_numbers)
