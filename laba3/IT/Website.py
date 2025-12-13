class Website:
    def __init__(self, domain, status="online", version="1.0"):
        self.domain = domain
        self.__status = status  # "online", "maintenance", "down"
        self.version = version

    def go_online(self):
        self.__status = "online"
        return f"Сайт {self.domain} теперь онлайн"

    def go_maintenance(self):
        self.__status = "maintenance"
        return f"Сайт {self.domain} на техобслуживании"

    def is_online(self):
        return self.__status == "online"

    def get_status(self):
        return self.__status

    def get_info(self):
        return f"Сайт: {self.domain} | Статус: {self.__status} | Версия: {self.version}"