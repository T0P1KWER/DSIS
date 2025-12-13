from Humans.Internet_shop_worker import Internet_shop_worker


class Director(Internet_shop_worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, branch, count_worker):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.__branch = branch
        self.__budget = 0
        self.__count_workers = count_worker
        self.__karma = 0
        self.__max_budget_history = 0  # для логики кармы

    def set_budget(self, budget):
        """Устанавливает бюджет с проверкой обоснованности"""
        if not isinstance(budget, (int, float)):
            print("Ошибка: бюджет должен быть числом")
            return

        if budget < 0:
            print("Ошибка: бюджет не может быть отрицательным")
            return

        old_budget = self.__budget

        # Логика кармы: увеличиваем только при обоснованном росте
        if budget > self.__max_budget_history:
            # Новый рекорд бюджета - хорошо
            self.__karma += 2
            self.__max_budget_history = budget
            print(f"✓ Установлен рекорд бюджета! Карма: {self.__karma}")
        elif budget < old_budget:
            # Уменьшение бюджета - обычно плохо
            self.__karma -= 1
            print(f"⚠ Бюджет уменьшен. Карма: {self.__karma}")
        elif budget == old_budget:
            # Без изменений
            print(f"Бюджет не изменился. Карма: {self.__karma}")
        else:
            # Рост, но не рекордный
            self.__karma += 1
            print(f"✓ Бюджет увеличен. Карма: {self.__karma}")

        self.__budget = budget
        print(f"Бюджет филиала '{self.__branch}' установлен: {self.__budget} руб.")

    def get_budget(self):
        return self.__budget

    def get_workers_count(self):
        return self.__count_workers

    def get_karma(self):
        return self.__karma

    def make_decision(self):
        return f"Директор {self.lastname} принимает стратегические решения по филиалу '{self.__branch}'"

    def approve_budget(self):
        return f"Директор {self.lastname} утверждает бюджет в размере {self.__budget} руб."

    def collaborate_with_accountant(self, accountant):
        """Взаимодействие с бухгалтером"""
        if not isinstance(accountant, Accountant):
            print("Ошибка: передан не бухгалтер!")
            return

        budget = self.__budget
        workers_count = self.__count_workers

        print(f"Директор {self.lastname} взаимодействует с бухгалтером {accountant.get_name()}")
        print(f"Переданы данные: бюджет={budget} руб., сотрудников={workers_count}")

        # Бухгалтер сам решает, как распределять
        result = accountant.distribute_money(budget, workers_count)
        print(f"Результат распределения: {result}")

    def hire_worker(self):
        self.__count_workers += 1
        self.__karma += 1
        print(f"Новый сотрудник нанят в распоряжение. Всего сотрудников: {self.__count_workers}")
        print(f"Карма увеличилась: {self.__karma}")

    def fire_worker(self):
        if self.__count_workers > 0:
            self.__count_workers -= 1
            self.__karma -= 2
            print(f"Сотрудник уволен. Осталось сотрудников: {self.__count_workers}")
            print(f"Карма уменьшилась: {self.__karma}")
        else:
            print("Некого увольнять!")


