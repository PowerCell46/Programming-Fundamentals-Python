class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if self.capacity > 0:
            self.capacity -= 1
            self.storage.append(product)
    def get_products(self):
        return self.storage
