number_of_electrons = int(input())
eletrons_list = []
position_of_the_shell = 0

while number_of_electrons > 0:
    position_of_the_shell += 1
    maximum_electrons_for_current_shell = 2 * position_of_the_shell * position_of_the_shell

    if number_of_electrons - maximum_electrons_for_current_shell > 0:
        number_of_electrons -= maximum_electrons_for_current_shell
        eletrons_list.append(maximum_electrons_for_current_shell)
    else:
        eletrons_list.append(number_of_electrons)
        number_of_electrons = 0

print(eletrons_list)