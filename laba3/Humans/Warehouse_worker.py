from Humans.Internet_shop_worker import Internet_shop_worker


class Warehouse_worker(Internet_shop_worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, department, team_size):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.__department = department
        self.__team_size = team_size

    def load_boxes(self, box_count):
        print(f"Грузчик {self.name} погрузил {box_count} коробок.")

    def report_team_size(self):
        return f"В команде грузчика {self.name} {self.__team_size} человек."
