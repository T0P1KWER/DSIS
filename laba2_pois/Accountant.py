from Postal_Worker import Postal_Worker
class Accountant(Postal_Worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, accounting_software, clients_count):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.__accounting_software = accounting_software
        self.__clients_count = clients_count
    def use_accounting(self):
        print(f"Бухгалтер {self.name} использует программу {self.__accounting_software}")
    def process_payments(self):
        return f"Обрабатывает платежи для {self.__clients_count} клиентов"
    def distribute_money(self, budget, people_count):
        if people_count > 0:
            amount_per_person = budget / people_count
            return f"Бюджет {budget} руб. распределен между {people_count} людьми. По {amount_per_person:.2f} руб. на человека"
        else:
            return "Некому распределять деньги!"