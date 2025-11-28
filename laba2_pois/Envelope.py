class Envelope:
    def __init__(self):
        self.size = "C4"
        self.color = "белый"
        self.is_sealed = False
    
    def seal(self):
        self.is_sealed = True
        return "Конверт запечатан"