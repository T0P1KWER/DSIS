from Humans.Human import Human


from Errors.Invalid_worker_id_error import Invalid_worker_id_error


class Internet_shop_worker(Human):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience):
        super().__init__(name, lastname, surname, age, gender, height, weight)
        self.__ownskills = ownskills
        self.__education = education
        self.__status = status
        self.__work_experience = work_experience
        self.__salary = 1000

        # Валидация ID при создании
        self.set_worker_id(worker_id)

    def set_worker_id(self, worker_id):
        try:
            if not worker_id or not str(worker_id).strip():
                raise invalid_worker_id_error("ID сотрудника не может быть пустым!")
            if not isinstance(worker_id, str) or len(worker_id) < 3:
                raise invalid_worker_id_error("ID сотрудника должен быть строкой минимум из 3 символов!")
            self.worker_id = worker_id
        except invalid_worker_id_error as e:
            print(f"Ошибка ID: {e}")
            self.worker_id = "UNKNOWN"

    def tell_about_yourself_like_a_work(self):
        info = f"""
        === РАБОЧАЯ ИНФОРМАЦИЯ ===
        ID сотрудника: {self.worker_id}
        ФИО: {self.lastname} {self.name} {self.surname}
        статус: {self.__status}
        Образование: {self.__education}
        Навыки: {self.__ownskills}
        Стаж: {self.__work_experience} лет
        Возраст: {self.age} лет
        """
        return info

    def promote(self, new_status, salary_increase=0):
        old_status = self.__status
        self.__status = new_status
        self.__salary += salary_increase
        self.__work_experience += 0.5
        return f" Повышение! {old_status} → {new_status}. Зарплата: {self.__salary} руб."

    def demote(self, new_status, salary_decrease=0):
        old_status = self.__status
        self.__status = new_status
        self.__salary = max(1000, self.__salary - salary_decrease)
        return f" Понижение! {old_status} → {new_status}. Зарплата: {self.__salary} руб."

    def get_salary_info(self):
        return f"Текущая зарплата: {self.__salary} руб."

    def set_salary(self, new_salary):
        self.__salary = new_salary
        return f"Зарплата установлена: {new_salary} руб."