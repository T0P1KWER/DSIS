class Stamp:
    def __init__(self):
        self.stamp_type = "служебная"
        self.ink_color = "фиолетовый"
        self.owner = "Почта России"
    
    def make_impression(self):
        return f"Поставлена {self.stamp_type} печать"