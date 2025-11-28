from Transport import Transport
from CarNotOK import CarNotOK
from PostManError import PostmanError
from NegativeMileageError import NegativeMileageError
from TooBigMileageError import TooBigMileageError

class Car(Transport):
    def __init__(self, horsepower, weight, tipe, brand, model, year, price):
        super().__init__(horsepower, weight, tipe)
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__mileage = 0
        self.__current_driver = None
        super().set_price(price)

    def assign_to_postman(self, postman):
        try:
            if not super().get_serviceability():
                raise CarNotOK("Автомобиль неисправен!")

            if not postman:
                raise PostmanError("Почтальон не указан!")

            self.__current_driver = postman
            return f"Автомобиль {self.get_brand_model()} назначен почтальону {postman.lastname}"

        except PostmanError:
            return f"Ошибка назначения: {PostmanError}"
        except CarNotOK:
            return f"Ошибка назначения: {CarNotOK}"

    def add_mileage(self, km):
        try:
            if km <= 0:
                raise NegativeMileageError("Пробег должен быть положительным числом!")

            if km > 1000:
                raise TooBigMileageError("Слишком большой пробег за один раз!")

            self.__mileage += km
            return f"Добавлено {km} км к пробегу"

        except NegativeMileageError:
            return f"Ошибка добавления пробега: {NegativeMileageError}"
        except TooBigMileageError:
            return f"Ошибка добавления пробега: {TooBigMileageError}"

    def get_brand_model(self):
        return f"{self.__brand} {self.__model}"

    def get_mileage(self):
        return self.__mileage

    def get_info(self):
        return f"{self.get_brand_model()} - {super().check_serviceability()}"