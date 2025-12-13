from Humans.Internet_shop_worker import Internet_shop_worker
class Accountant(Internet_shop_worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, accounting_software, clients_count):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.__accounting_software = accounting_software
        self.__clients_count = clients_count

    def get_name(self):
        return self.name

    def use_accounting(self):
        print(f"Бухгалтер {self.name} использует программу {self.__accounting_software}")

    def process_payments(self):
        return f"Бухгалтер {self.name} обрабатывает платежи для {self.__clients_count} клиентов"

    def distribute_money(self, total_budget, people_count):
        print(f"Бухгалтер {self.name} начинает распределение бюджета...")

        if not isinstance(total_budget, (int, float)) or total_budget <= 0:
            return "Ошибка: некорректный бюджет"

        if not isinstance(people_count, int) or people_count <= 0:
            return "Ошибка: некорректное количество сотрудников"
        administrative_costs = total_budget * 0.1
        salary_pool = total_budget - administrative_costs

        if people_count > 0:
            amount_per_person = salary_pool / people_count
            return (f"Бюджет {total_budget} руб. распределен:\n"
                    f"• Административные расходы: {administrative_costs:.2f} руб.\n"
                    f"• Фонд оплаты труда: {salary_pool:.2f} руб.\n"
                    f"• На {people_count} сотрудников: по {amount_per_person:.2f} руб./чел.")
        else:
            return "Некому распределять деньги!"

    def add_client(self):
        self.__clients_count += 1
        print(f"Добавлен новый клиент. Всего клиентов: {self.__clients_count}")

    def get_clients_count(self):
        return self.__clients_count


    def set_department(self, department):
        if hasattr(department, 'has_safe'):
            self._department = department
        else:
            print("Ошибка: отдел не поддерживает функции бухгалтерии")