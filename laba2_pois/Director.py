from Postal_Worker import Postal_Worker


class Director(Postal_Worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, branch,count_worker):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.__branch = branch  # филиал управления
        self.__budget = 0 # бюджет филиала
        self.__count_workers=count_worker
        self.__karma=0

    def set_budget(self, budget):
        if not isinstance(budget, (int, float)):
            print("Ошибка: бюджет должен быть числом")
            return

        if budget < 0:
            print("Ошибка: бюджет не может быть отрицательным")
            return

        # Увеличиваем карму если бюджет уменьшается
        if budget < self.__budget:
            self.__karma -= 1
            print(f" Бюджет уменьшен. Карма: {self.__karma}")
        else:
            self.__karma+=1
            print(f" Бюджет увеличен. Карма: {self.__karma}")

        self.__budget = budget
        print(f"Бюджет установлен: {self.__budget} руб.")

    def make_decision(self):
        return f"Директор {self.lastname} принимает стратегические решения"

    def get_budget(self):
        return self.__budget

    def get_workers_count(self):

        return self.__count_workers

    def make_decision(self):
        return f"Директор {self.lastname} принимает стратегические решения"

    def approve_budget(self):
        return f"Утверждает бюджет в размере {self.__budget} руб."

    def collaborate_with_accountant(self, accountant):
        budget = self.get_budget()
        workers_count = self.get_workers_count()
        if budget and workers_count:
            result = accountant.distribute_money(budget, workers_count)
            print(f"Директор {self.lastname} передал бюджет бухгалтеру {accountant.name}")
            print(result)

    def sell_office(self, post_office):
        if self.__karma < -10:
            post_office.sell_office()
            print(f"Офис продан! Карма директора: {self.__karma}")
        else:
            print(f"Недостаточно плохая карма: {self.__karma}. Нужно меньше -10")