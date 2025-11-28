from Postal_Worker import Postal_Worker
class Watchman (Postal_Worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, security_clearance, weapon_license ):

        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,work_experience)
        self.__security_clearance = security_clearance  # уровень доступа
        self.__weapon_license = weapon_license  # наличие лицензии на оружие
        self.__is_armed = False
    def issue_weapon(self, weapon_type):
        if self.__weapon_license:
            self.__is_armed = True
            return f" Охраннику {self.lastname} выдано: {weapon_type}"
        else:
            return f" Невозможно выдать оружие. Отсутствует лицензия"

    def return_weapon(self):
        if self.__is_armed:
            self.__is_armed = False
            return f" Охранник {self.lastname} сдал оружие"
        return f"ℹ Охранник {self.lastname} не вооружен"

    def get_weapon_status(self):
        status = "вооружен" if self.__is_armed else "не вооружен"
        return f"Охранник {self.lastname}: {status}"