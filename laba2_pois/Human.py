class Human:
    def __init__(self, name, lastname, surname, age, gender, height, weight):
        self.name = name
        self.lastname = lastname
        self.surname = surname
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.__is_alive = True
        self.__ownskills = []
        self._education = ""

    def tell_about_yourself(self):
        if not self.__is_alive:
            print(f"{self.name} больше не с нами...")
            return
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.lastname}")
        print(f"Отчество: {self.surname}")
        print(f"Возраст: {self.age}")
        print(f"Пол: {self.gender}")
        print(f"Рост: {self.height}")
        print(f"Вес: {self.weight}")
        print(f"Навыки: {self.__ownskills}")
        print(f"Образование: {self._education}")

    def die(self):
        self.__is_alive = False
        print(f"человек {self.name} {self.lastname} помер")

    def is_alive(self):
        return self.__is_alive