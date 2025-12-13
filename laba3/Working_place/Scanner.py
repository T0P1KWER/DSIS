class Scanner:
    def __init__(self):
        self.resolution = "600dpi"
        self.scan_speed = 10
        self.is_duplex = True
    
    def scan_document(self, document):
        return f"Документ '{document}' отсканирован с разрешением {self.resolution}"
    
    def check_status(self):
        return f"Сканер готов к работе, разрешение: {self.resolution}"