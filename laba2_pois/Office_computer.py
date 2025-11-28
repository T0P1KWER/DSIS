from Computer import Computer
class Office_computer(Computer):
    def __init__(self):
        super().__init__()
        self.computer_id = "OFFICE-PC-001"

    def work(self):
        return f"Офисный компьютер {self.computer_id} работает "
