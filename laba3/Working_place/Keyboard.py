class Keyboard:
    def __init__(self):
        self.layout = "QWERTY"
        self.keys_count = 104
        self.is_wireless = False
    
    def type_text(self, text):
        return f"Набрано: {text}"