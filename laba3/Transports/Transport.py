class Transport:
    def __init__(self, horsepower, weight, tipe):
        self.__horsepower = horsepower
        self.__weight = weight
        self.__type = tipe
        self.__price = 0
        self.__serviceability = True  # по умолчанию исправен

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def get_serviceability(self):
        return self.__serviceability

    def check_serviceability(self):
        return "Исправен" if self.__serviceability else "Неисправен"

    def break_down(self):
        self.__serviceability = False

    def repair(self):
        self.__serviceability = True