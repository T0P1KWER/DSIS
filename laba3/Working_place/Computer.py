class Computer:
    def __init__(self):
        self.owner_name = "Иван Иванов"  # 1 поле

    def who_owner(self):  # 1 метод
        return f"Владелец- {self.owner_name} "
