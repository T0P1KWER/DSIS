from Errors.Empty_name_error import Empty_name_error
from Errors.Invalid_age_error import Invalid_age_error
from Errors.Invalid_height_error import Invalid_height_error
from Errors.Invalid_weight_error import Invalid_weight_error
from Errors.Invalid_gender_error import Invalid_gender_error


class Human:
    def __init__(self, name, lastname, surname, age, gender, height, weight):
        self.set_name(name)
        self.lastname = lastname
        self.surname = surname
        self.set_age(age)
        self.set_gender(gender)
        self.set_height(height)
        self.set_weight(weight)

        self.__is_alive = True
        self.__ownskills = []
        self._education = ""

    def set_name(self, name):
        if not name or not name.strip():
            raise Empty_name_error("Имя не может быть пустым!")
        self.name = name

    def set_age(self, age):
        if not isinstance(age, int) or age < 0 or age > 150:
            raise Invalid_age_error("Возраст должен быть целым числом от 0 до 150!")
        self.age = age

    def set_gender(self, gender):
        valid = ["м", "ж", "мужской", "женский", "male", "female"]
        if str(gender).lower() not in valid:
            raise Invalid_gender_error("Некорректный пол! Используйте: м/ж, мужской/женский")
        self.gender = gender

    def set_height(self, height):
        if not isinstance(height, (int, float)) or height <= 0 or height > 300:
            raise Invalid_height_error("Рост должен быть положительным числом (макс. 300 см)!")
        self.height = height

    def set_weight(self, weight):
        if not isinstance(weight, (int, float)) or weight <= 0 or weight > 1000:
            raise Invalid_weight_error("Вес должен быть положительным числом (макс. 1000 кг)!")
        self.weight = weight

    def tell_about_yourself(self):
        if not self.__is_alive:
            print(f"{self.name} больше не с нами...")
            return
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.lastname}")
        print(f"Отчество: {self.surname}")
        print(f"Возраст: {self.age}")
        print(f"Пол: {self.gender}")
        print(f"Рост: {self.height} см")
        print(f"Вес: {self.weight} кг")
        print(f"Навыки: {self.__ownskills}")
        print(f"Образование: {self._education}")

    def die(self):
        self.__is_alive = False
        print(f"Человек {self.name} {self.lastname} умер.")

    def is_alive(self):
        return self.__is_alive