from Postal_Worker import Postal_Worker


class Manager(Postal_Worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, department, team_size):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.__department = department  # отдел управления
        self.__team_size = team_size  # размер команды

    def manage_team(self):
        return f"Менеджер {self.lastname} управляет отделом {self.__department}"

    def conduct_meeting(self):
        return f"Команда состоит из {self.__team_size} человек"