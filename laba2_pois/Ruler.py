class Ruler:
    def __init__(self):
        self.length = 30
        self.material = "пластик"
        self.units = "см"
    
    def measure(self, length):
        return f"Измерено: {length} {self.units}"