from Human import Human
class PostalWorker(Human):
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.email = ""

    def input_data(self):
        """Метод для ввода данных работника"""
        self.name = input("Введите имя работника: ")
        self.phone = input("Введите телефон работника: ")
        self.email = input("Введите email работника: ")
        return "Данные сохранены!"