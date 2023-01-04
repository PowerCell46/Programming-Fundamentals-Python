distances = input().split()
distances_to_the_pokemons = [int(pokemon) for pokemon in distances]
collected_pokemons = 0

while True:
    index_for_current_pokemon = int(input())
    if index_for_current_pokemon < 0:
        current_pokemon_value = distances_to_the_pokemons.pop(0)
        distances_to_the_pokemons.insert(0, distances_to_the_pokemons[len(distances_to_the_pokemons) - 1])
    elif index_for_current_pokemon >= len(distances_to_the_pokemons):
        current_pokemon_value = distances_to_the_pokemons.pop()
        distances_to_the_pokemons.insert(len(distances_to_the_pokemons), distances_to_the_pokemons[0])
    else:
        current_pokemon_value = distances_to_the_pokemons.pop(index_for_current_pokemon)

    collected_pokemons += current_pokemon_value
    distances = []
    for i in range(0, len(distances_to_the_pokemons)):

        current_pokemon_value_1 = distances_to_the_pokemons[i]
        if current_pokemon_value_1 <= current_pokemon_value:
            current_pokemon_value_1 += current_pokemon_value
            distances.append(current_pokemon_value_1)
        else:
            current_pokemon_value_1 -= current_pokemon_value
            distances.append(current_pokemon_value_1)

    distances_to_the_pokemons = distances
    if len(distances_to_the_pokemons) == 0:
        break

print(collected_pokemons)
