from Room import Room
class Canteen(Room):
    def __init__(self, square):
        super().__init__(square)
        self.tables_count = 45

    def serve_lunch(self):
        return f"Обед подается на {self.tables_count} столах"
