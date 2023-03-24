countries = str(input()).split(", ")
cities = str(input()).split(", ")

capitals_dictionary = {}

for i in range(0, len(countries)):
    capitals_dictionary[countries[i]] = cities[i]

for key, value in capitals_dictionary.items():
    print(f'{key} -> {value}')
