class Mailbox:
    def __init__(self, box_number, capacity, location):
        self.box_number = box_number
        self.capacity = capacity
        self.location = location
        self.current_letters = 0

    def add_letter(self):
        if self.current_letters < self.capacity:
            self.current_letters += 1
            return f"Письмо добавлено в ящик {self.box_number}"
        else:
            return "Ящик полон!"

    def collect_letters(self):
        collected = self.current_letters
        self.current_letters = 0
        return f"Забрано {collected} писем"