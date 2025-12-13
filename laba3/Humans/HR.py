from Humans.Human import Human
from Humans.Internet_shop_worker import Internet_shop_worker

class HR(Human):
    def __init__(self, name, lastname, surname, age, gender, height, weight,
                 hr_id, experience_years, hiring_quota, department=None, hired_workers=None):
        # 5 полей: hr_id, experience_years, hiring_quota, department, hired_workers
        super().__init__(name, lastname, surname, age, gender, height, weight)
        self.hr_id = hr_id
        self.experience_years = experience_years
        self.hiring_quota = hiring_quota
        self._department = department
        self._hired_workers = hired_workers if hired_workers is not None else []

    def hire_worker(self, name, lastname, surname, age, gender, height, weight,
                    worker_id, ownskills, education, status, work_experience):
        if len(self._hired_workers) >= self.hiring_quota:
            return "Лимит найма исчерпан!"

        new_worker = Internet_shop_worker(
            name, lastname, surname, age, gender, height, weight,
            worker_id, ownskills, education, status, work_experience
        )
        self._hired_workers.append(new_worker)
        return f"HR {self.name} нанял сотрудника {lastname} {name}"

    def set_department(self, department):
        self._department = department

    def get_hired_count(self):
        return len(self._hired_workers)