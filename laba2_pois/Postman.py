from Postal_Worker import Postal_Worker


class Postman(Postal_Worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, delivery_zone, transport_type):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.__delivery_zone = delivery_zone
        self.__transport_type = transport_type
        self.__office = None
        self.__assigned_vehicle = None  # универсальное поле для любого транспорта

    def assign_vehicle(self, vehicle):
        """Универсальный метод для назначения ЛЮБОГО транспорта"""
        if self.__assigned_vehicle:
            print(f"Освобождаем предыдущий транспорт")

        self.__assigned_vehicle = vehicle
        result = vehicle.assign_to_postman(self)  # используем единый метод
        print(result)

    def make_delivery(self, distance_km):
        """Универсальный метод доставки на любом транспорте"""
        if self.__assigned_vehicle and self.__assigned_vehicle.get_serviceability():
            self.__assigned_vehicle.add_mileage(distance_km)
            vehicle_info = self.__assigned_vehicle.get_info()
            return f"Почтальон {self.lastname} проехал {distance_km} км на {vehicle_info}"
        return f"Почтальон {self.lastname} не может выполнить доставку"

    def get_vehicle_info(self):
        """Универсальный метод получения информации о транспорте"""
        if self.__assigned_vehicle:
            return f"Транспорт: {self.__assigned_vehicle.get_info()}"
        return "Транспорт не назначен"

    # Существующие методы
    def set_office(self, new_office):
        if self.__office is not None:
            self.__office.remove_postman(self)
        self.__office = new_office
        new_office.add_postman(self)

    def get_office(self):
        return self.__office

    def deliver_packages(self):
        office_info = f" из офиса {self.__office.address}" if self.__office else ""
        vehicle_info = f" на {self.__assigned_vehicle.get_brand_model()}" if self.__assigned_vehicle else " пешком"
        return f"Почтальон {self.lastname} доставляет в {self.__delivery_zone}{office_info}{vehicle_info}"