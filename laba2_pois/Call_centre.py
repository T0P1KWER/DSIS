from Room import Room
class Call_centre(Room):
    def __init__(self, square, operators_count, phone_lines, workstations):
        super().__init__(square)
        self.operators_count = operators_count
        self.phone_lines = phone_lines
        self.workstations = workstations

    def handle_calls(self):
        return "Прием звонков от клиентов"