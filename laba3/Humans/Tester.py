from Humans.Internet_shop_worker import Internet_shop_worker

class Tester(Internet_shop_worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, test_cases_written):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.test_cases_written = test_cases_written  #


    def test_feature(self, feature_name):
        return f"Тестировщик {self.name} тестирует функцию: {feature_name}"