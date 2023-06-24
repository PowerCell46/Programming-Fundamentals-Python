dwarfs = {}

while True:
    current_input = input()
    if current_input == "Once upon a time":
        break
    current_input = current_input.split(" <:> ")
    dwarf_name = current_input[0]
    dwarf_hat_color = current_input[1]
    dwarf_physics = int(current_input[2])
    if dwarf_hat_color not in dwarfs.keys():
        dwarfs[dwarf_hat_color] = {dwarf_name: dwarf_physics}
    else:
        if dwarf_name not in dwarfs[dwarf_hat_color].keys():
            dwarfs[dwarf_hat_color][dwarf_name] = dwarf_physics
        else:
            if dwarf_physics > dwarfs[dwarf_hat_color][dwarf_name]:
                dwarfs[dwarf_hat_color][dwarf_name] = dwarf_physics

ordered_dwarfs = []

for hat_color, dwarf_info in dwarfs.items():
    total_count = len(dwarf_info)
    for dwarf_name, dwarf_physics in dwarf_info.items():
        ordered_dwarfs.append((dwarf_name, dwarf_physics, hat_color, total_count))

ordered_dwarfs.sort(key=lambda x: (x[1], x[3]), reverse=True)

for dwarf in ordered_dwarfs:
    print(f'({dwarf[2]}) {dwarf[0]} <-> {dwarf[1]}')
    
