from Room import Room
class Main_hall(Room):
    def __init__(self, square, windows_count, seats_count):
        super().__init__(square)
        self.windows_count = windows_count
        self.seats_count = seats_count

    def get_hall_capacity(self):
        return f"Вместимость зала: {self.seats_count} человек"