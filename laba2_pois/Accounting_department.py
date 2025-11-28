from Room import Room

class Accounting_department(Room):
    def __init__(self, square, computers_count, safe_available):
        super().__init__(square)
        self.computers_count = computers_count
        self.safe_available = safe_available

