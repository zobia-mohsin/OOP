class Retailitem:

    def __init__(self, item_desc, units, price):
        self.__item_desc = item_desc
        self.__units = units
        self.__price = price

    def set_description(self, item_desc):
        self.__item_desc = item_desc

    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__item_desc

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price
