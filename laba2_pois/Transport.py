class Transport:
    def __init__(self, horsepower, weight, tipe):
        self.__horsepower = horsepower
        self.__weight = weight
        self.__tipe = tipe
        self.__serviceability = True
        self.__price = 0

    def check_serviceability(self):
        return "Исправен" if self.__serviceability else "Неисправен"

    def break_down(self):
        self.__serviceability = False
        return "Транспорт сломан"

    def repair(self):
        self.__serviceability = True
        return "Транспорт отремонтирован"

    def get_horsepower(self): return self.__horsepower
    def get_weight(self): return self.__weight
    def get_tipe(self): return self.__tipe
    def get_serviceability(self): return self.__serviceability
    def get_price(self): return self.__price
    def set_price(self, new_price): self.__price = new_price