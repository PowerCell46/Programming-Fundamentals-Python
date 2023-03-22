class Party:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def __repr__(self):
        return_string = f'Going: {", ".join(self.people)}'
        return_string += "\nTotal: " + str(len(self.people))
        return return_string

current_party = Party()

while True:
    current_line = str(input())
    if current_line == "End":
        break
    current_party.add_person(current_line)

print(current_party)
