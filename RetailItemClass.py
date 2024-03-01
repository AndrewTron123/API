class RetailItemClass:
    def __init__(self, item_description, units_inventory, price):
        self.__item_description = item_description
        self.__units_inventory = units_inventory
        self.__price = price

    def display_info(self):
        item_description = self.__item_description
        units_inventory = self.__units_inventory
        price = self.__price
        print(f'Description: {item_description},  Units in Inventory: {units_inventory},  Price: {price}')