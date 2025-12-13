from Chair import Chair
from Cabinet import Cabinet
from Table import Table
from Scanner import Scanner
from Printer import Printer
from Monitor import Monitor
from Keyboard import Keyboard


class Working_place:
    def __init__(self):
        self.chair = Chair("Офисный стул")
        self.table = Table("Рабочий стол")
        self.cabinet = Cabinet("Файловый шкаф")
        self.printer = Printer()
        self.keyboard = Keyboard()
        self.monitor = Monitor()
        self.scanner = Scanner()

    def get_full_workplace_info(self):
        info = "=== ПОЛНАЯ ИНФОРМАЦИЯ О РАБОЧЕМ МЕСТЕ ===\n"
        # Мебель
        info += f"Мебель: {self.chair.sit_on_chair()}, {self.table.info()}, {self.cabinet.store_items()}\n"
        # Техника
        info += f"Техника: {self.monitor.display_status()}, {self.keyboard.type_keys()}, {self.printer.status()}, {self.scanner.check_status()}\n"
        return info