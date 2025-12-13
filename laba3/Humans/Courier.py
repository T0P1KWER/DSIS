from Humans.Internet_shop_worker import Internet_shop_worker

class Courier(Internet_shop_worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, delivery_zone, transport_type):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.__delivery_zone = delivery_zone
        self.__transport_type = transport_type
        self.__assigned_transport = None

    def assign_transport(self, transport):
        self.__assigned_transport = transport
        transport.assign_to_courier(self)

    def get_delivery_zone(self):
        return self.__delivery_zone

    def get_transport_info(self):
        if self.__assigned_transport:
            return self.__assigned_transport.get_info()
        return "Транспорт не назначен"