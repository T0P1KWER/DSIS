from Humans.Human import Human
class Supplier(Human):
    def __init__(self, name, lastname, surname, age, gender, height, weight, cooperation_years, supplies):
        super().__init__(name, lastname, surname, age, gender, height, weight)
        self.__cooperation_years = cooperation_years
        self.__supplies = supplies
    def get_cooperation_years(self):
        return self.__cooperation_years
    def get_supplies(self):
        return self.__supplies
    def get_info(self):
        return f"Поставщик: {self.lastname} {self.name}\n" \
               f"Сотрудничество: {self.__cooperation_years} лет\n" \
               f"Поставляет: {self.__supplies}"