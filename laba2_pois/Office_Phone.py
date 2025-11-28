class Office_Phone:
    def __init__(self):
        self.phone_number = "555-0123"  # 1 поле

    def make_call(self):  # 1 метод
        return f"Звонок с номера: {self.phone_number}"