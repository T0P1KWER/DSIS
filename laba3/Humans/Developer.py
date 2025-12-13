
from Humans.Internet_shop_worker import Internet_shop_worker
from Errors.Name_error import Name_error
class Developer(Internet_shop_worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, main_language, project_count):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.main_language = main_language
        self.project_count = project_count

    def write_code(self, task):
         try:
             if self.name=="robot":
                 raise Name_error("ошиька")
             return f"Разработчик {self.name} пишет код для задачи: {task}"
         except Name_error:
             return f"Ощибка: {Name_error}"