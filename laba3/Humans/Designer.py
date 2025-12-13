from Humans.Internet_shop_worker import Internet_shop_worker

class Designer(Internet_shop_worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, design_tool):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.design_tool = design_tool

    def create_mockup(self, page_name):
        return f"Дизайнер {self.name} создаёт макет страницы: {page_name}"