countries = str(input()).split(", ")
cities = str(input()).split(", ")

countries_list = [country for country in countries]
cities_list = [city for city in cities]

capitals_dictionary = dict(zip(countries_list, cities_list))

for key, value in capitals_dictionary.items():
    print(f'{key} -> {value}')

