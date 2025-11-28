class Pencil:
    def __init__(self):
        self.hardness = "HB"
        self.length = 15
        self.with_eraser = True
    
    def draw(self):
        return f"Карандаш {self.hardness} рисует"