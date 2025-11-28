class Pen:
    def __init__(self):
        self.ink_color = "синий"
        self.ink_level = 100
        self.brand = "Parker"
    
    def write(self, text):
        return f"Ручка пишет: {text}"