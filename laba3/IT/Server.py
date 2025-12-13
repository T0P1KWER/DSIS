class Server:
    def __init__(self, ip_address, capacity_gb, server_type="web"):
        self.ip_address = ip_address
        self.capacity_gb = capacity_gb
        self.__server_type = server_type  # "web", "database", "backup"
        self.__is_running = True
        self.__load_percent = 0

    def start(self):
        self.__is_running = True
        return f"Сервер {self.ip_address} запущен"

    def shutdown(self):
        self.__is_running = False
        return f"Сервер {self.ip_address} выключен"

    def is_running(self):
        return self.__is_running

    def set_load(self, percent):
        if 0 <= percent <= 100:
            self.__load_percent = percent

    def get_load(self):
        return self.__load_percent

    def get_info(self):
        status = "Работает" if self.__is_running else "Выключен"
        return f"Сервер {self.ip_address} ({self.__server_type}) | Статус: {status} | Нагрузка: {self.__load_percent}%"