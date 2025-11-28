from Transport import Transport


class Bicycle(Transport):
    def __init__(self, horsepower, weight, tipe, brand, model, year, price):
        super().__init__(horsepower, weight, tipe)
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__mileage = 0
        self.__current_rider = None
        super().set_price(price)

    def assign_to_postman(self, postman):
        """Единый метод связи с почтальоном"""
        if super().get_serviceability():
            self.__current_rider = postman
            return f"Велосипед {self.get_brand_model()} назначен почтальону {postman.lastname}"
        return "Велосипед неисправен!"

    def add_mileage(self, km):
        if km > 0:
            self.__mileage += km

    def get_brand_model(self):
        return f"{self.__brand} {self.__model}"

    def get_mileage(self):
        return self.__mileage

    def get_info(self):
        return f"{self.get_brand_model()} - {super().check_serviceability()}"