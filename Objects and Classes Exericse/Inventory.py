class Inventory:
    def __init__(self, __capacity):
        self.items = []
        self.__capacity = __capacity
        self.current_capacity = __capacity

    def add_item(self, item):
        if self.current_capacity > 0:
            self.current_capacity -= 1
            self.items.append(item)

        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return_string = "Items: "
        return_string += ", ".join(self.items)
        return_string += ".\nCapacity left: " + str(self.current_capacity)
        return return_string
