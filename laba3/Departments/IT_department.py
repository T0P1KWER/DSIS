from Departments.Department import Department
from Working_place import Working_place
from IT.Website import Website
from IT.Server import Server


class IT_department(Department):
    def __init__(self, square, monthly_budget, initial_workplaces=0):
        super().__init__(square)
        self.monthly_budget = monthly_budget
        self.__working_status = "working"
        self.__it_workers = []
        self.__workplaces = []
        self.__servers = []
        self.__website = None

        for _ in range(initial_workplaces):
            self.add_workplace()
    def add_workplace(self):
        new_place = Working_place()
        self.__workplaces.append(new_place)
        print(f"Добавлено IT-рабочее место. Всего: {len(self.__workplaces)}")

    def get_workplaces_count(self):
        return len(self.__workplaces)

    def add_server(self, ip_address, capacity_gb, server_type="web"):
        new_server = Server(ip_address, capacity_gb, server_type)
        self.__servers.append(new_server)
        print(f"Добавлен сервер {ip_address}. Всего серверов: {len(self.__servers)}")

    def get_servers_count(self):
        return len(self.__servers)

    def get_server_info(self, index=0):
        if 0 <= index < len(self.__servers):
            return self.__servers[index].get_info()
        return "Сервер не найден"

    def set_website(self, domain, version="1.0"):
        self.__website = Website(domain, "online", version)
        print(f"Сайт {domain} привязан к IT-отделу")

    def get_website_info(self):
        if self.__website:
            return self.__website.get_info()
        return "Сайт не настроен"

    def is_website_online(self):
        if self.__website:
            return self.__website.is_online()
        return False
    def add_it_worker(self, worker):
        from Humans.Internet_shop_worker import Internet_shop_worker
        if isinstance(worker, Internet_shop_worker) and worker not in self.__it_workers:
            self.__it_workers.append(worker)
            print(f"IT-специалист {worker.lastname} {worker.name} добавлен")
        else:
            print("Ошибка: только работники интернет-магазина")

    def get_workers_count(self):
        return len(self.__it_workers)

    def get_it_summary(self):
        info = f"=== IT-ОТДЕЛ ===\n"
        info += f"Площадь: {self.square} м² | Бюджет: {self.monthly_budget} руб.\n"
        info += f"Рабочих мест: {self.get_workplaces_count()}\n"
        info += f"Серверов: {self.get_servers_count()}\n"
        info += f"{self.get_website_info()}\n"
        info += f"Сотрудников: {self.get_workers_count()}"
        return info