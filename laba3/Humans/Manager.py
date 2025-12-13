from Humans.Internet_shop_worker import Internet_shop_worker


class Manager(Internet_shop_worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, department, team_size):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.__department = department
        self.__team_size = team_size

    def manage_team(self):
        return f"Менеджер {self.lastname} управляет отделом {self.__department}"

    def conduct_meeting(self):
        return f"Команда состоит из {self.__team_size} человек"