from Departments.Department import Department
from Working_place import Working_place  # ← новый импорт


class Office(Department):
    def __init__(self, square, price, working_grafic, initial_workplaces=0):
        super().__init__(square)
        self.__price = price
        self.working_grafic = working_grafic
        self.__working_status = "working"
        self.__workers = []
        self.__workplaces = []
        self.__count_of_workers = 0
        for _ in range(initial_workplaces):
            self.add_workplace()

    def add_workplace(self):
        new_place = Working_place()
        self.__workplaces.append(new_place)
        print(f"Добавлено новое рабочее место. Всего: {len(self.__workplaces)}")

    def remove_workplace(self):
        if self.__workplaces:
            self.__workplaces.pop()
            print(f"Рабочее место удалено. Осталось: {len(self.__workplaces)}")
        else:
            print("Нет рабочих мест для удаления")

    def get_workplaces_count(self):
        return len(self.__workplaces)

    def get_workplace_info(self, index=0):
        if 0 <= index < len(self.__workplaces):
            return self.__workplaces[index].get_full_workplace_info()
        return "Рабочее место не найдено"

    def add_worker(self, worker):
        from Humans.Internet_shop_worker import Internet_shop_worker
        if isinstance(worker, Internet_shop_worker) and worker not in self.__workers:
            self.__workers.append(worker)
            self.__count_of_workers += 1
            print(f"Работник {worker.lastname} {worker.name} принят в офис")
        else:
            print("Ошибка: можно добавлять только работников интернет-магазина")

    def remove_worker(self, worker):
        if worker in self.__workers:
            self.__workers.remove(worker)
            self.__count_of_workers -= 1
            print(f"Работник {worker.lastname} уволен из офиса")

    def get_workers_count(self):
        return self.__count_of_workers

    def list_worker_names(self):
        return [f"{w.lastname} {w.name}" for w in self.__workers]

    def is_open(self):
        return self.__working_status == "working"