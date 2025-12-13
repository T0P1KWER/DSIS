class Printer:
    def __init__(self):
        self.model = "HP LaserJet"
        self.paper_count = 50
        self.ink_level = 80
        self.is_online = True

    def print_document(self, document):
        if self.paper_count > 0 and self.ink_level > 0:
            self.paper_count -= 1
            self.ink_level -= 5
            return f"Документ '{document}' напечатан"
        return "Ошибка печати: проверьте бумагу или чернила"
    
    def status(self):
        return f"Принтер {self.model}: бумага - {self.paper_count}, чернила - {self.ink_level}%"