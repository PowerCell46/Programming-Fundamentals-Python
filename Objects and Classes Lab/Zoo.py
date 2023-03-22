class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):

        if species == "mammal":
            self.mammals.append(name)

        elif species == "fish":
            self.fishes.append(name)

        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f'Mammals in {self.name}: {", ".join(self.mammals)}\nTotal animals: {Zoo.__animals}'

        elif species == "fish":
            return f'Fishes in {self.name}: {", ".join(self.fishes)}\nTotal animals: {Zoo.__animals}'

        elif species == "bird":
            return f'Birds in {self.name}: {", ".join(self.birds)}\nTotal animals: {Zoo.__animals}'


name = str(input())
zoo_instance = Zoo(name)
number_of_lines = int(input())

while number_of_lines > 0:
    number_of_lines -= 1
    species, name = str(input()).split(" ")
    zoo_instance.add_animal(species, name)

species = str(input())
print(zoo_instance.get_info(species))
