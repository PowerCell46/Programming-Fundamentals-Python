class Catalogue:
    def __init__(self, name_of_the_catalogue):
        self.name = name_of_the_catalogue
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return_list = []
        for i in range(0, len(self.products)):
            if self.products[i][0] == first_letter:
                return_list.append(self.products[i])
        return return_list

    def __repr__(self):
        return_string = f'Items in the {self.name} catalogue:\n'
        return_string += '\n'.join(sorted(self.products))
        return  return_string
