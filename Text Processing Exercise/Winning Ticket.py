tickets = str(input()).split(", ")
searched_digit = ""
final_list_of_tickets = []

for ticket in tickets:
    final_current_ticket = ""
    for char in ticket:
        if char != "," and char != " ":
            final_current_ticket += char
    if len(final_current_ticket) > 0: # изчистваме всички запетайки и разстояния и ги апендваме към файнал лист
        final_list_of_tickets.append(final_current_ticket)


for ticket in final_list_of_tickets: # въртим всички билети
    if len(ticket) != 20: # ако броят на символите е различен от 20, продължаваме със следващия
        print(f'invalid ticket')
        continue
    first_half_ticket = ticket[:10]
    second_half_ticket = ticket[10:]
    first_half_occcurences = 0
    first_half_occcurences_list = [0]
    second_half_occurences = 0
    second_half_occurences_list = [0]

    if "@" in ticket:
        for digit in first_half_ticket:
            if digit == "@":
                first_half_occcurences += 1
                searched_digit = digit
            else:
                if first_half_occcurences > 0:
                    first_half_occcurences_list.append(first_half_occcurences)
                    first_half_occcurences = 0
        first_half_occcurences_list.append(first_half_occcurences)

        for digit in second_half_ticket:
            if digit == "@":
                searched_digit = digit
                second_half_occurences += 1
            else:
                if second_half_occurences > 0:
                    second_half_occurences_list.append(second_half_occurences)
                    second_half_occurences = 0
        second_half_occurences_list.append(second_half_occurences)

    if "#" in ticket:
        for digit in first_half_ticket:
            if digit == "#":
                first_half_occcurences += 1
                searched_digit = digit
            else:
                if first_half_occcurences > 0:
                    first_half_occcurences_list.append(first_half_occcurences)
                    first_half_occcurences = 0
        first_half_occcurences_list.append(first_half_occcurences)

        for digit in second_half_ticket:
            if digit == "#":
                searched_digit = digit
                second_half_occurences += 1
            else:
                if second_half_occurences > 0:
                    second_half_occurences_list.append(second_half_occurences)
                    second_half_occurences = 0
        second_half_occurences_list.append(second_half_occurences)

    if "$" in ticket:
        for digit in first_half_ticket:
            if digit == "$":
                first_half_occcurences += 1
                searched_digit = digit
            else:
                if first_half_occcurences > 0:
                    first_half_occcurences_list.append(first_half_occcurences)
                    first_half_occcurences = 0
        first_half_occcurences_list.append(first_half_occcurences)

        for digit in second_half_ticket:
            if digit == "$":
                searched_digit = digit
                second_half_occurences += 1
            else:
                if second_half_occurences > 0:
                    second_half_occurences_list.append(second_half_occurences)
                    second_half_occurences = 0
        second_half_occurences_list.append(second_half_occurences)

    if "^" in ticket:
        for digit in first_half_ticket:
            if digit == "^":
                first_half_occcurences += 1
                searched_digit = digit
            else:
                if first_half_occcurences > 0:
                    first_half_occcurences_list.append(first_half_occcurences)
                    first_half_occcurences = 0
        first_half_occcurences_list.append(first_half_occcurences)

        for digit in second_half_ticket:
            if digit == "^":
                searched_digit = digit
                second_half_occurences += 1
            else:
                if second_half_occurences > 0:
                    second_half_occurences_list.append(second_half_occurences)
                    second_half_occurences = 0
        second_half_occurences_list.append(second_half_occurences)


    if max(first_half_occcurences_list) >= 6 and max(second_half_occurences_list) >= 6: # проверяваме в двете половини на билета, дали има минимум 6 еднакви знака
        winning_counter_first_half = max(first_half_occcurences_list)
        winning_counter_second_half = max(second_half_occurences_list)

        if winning_counter_first_half == 10 and winning_counter_second_half == 10: # ако броят на еднаквите символи е 10 в двете половини, имаме Джакпот.
            print(f'ticket "{ticket}" - 10{first_half_ticket[0]} Jackpot!')
        else:
            list_of_occurences_no_jackpot = [winning_counter_first_half, winning_counter_second_half]
            print(f'ticket "{ticket}" - {min(list_of_occurences_no_jackpot)}{searched_digit}') # в другите случаи печатаме колко е печалбата от билета
    else:
        print(f'ticket "{ticket}" - no match') # ако в двете половини няма поне 6 еднакви знака, печатаме че няма мач
