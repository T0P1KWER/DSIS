from Chair import Chair
from Cabinet import Cabinet
from Table import Table
from Paper import Paper
from Pencil import Pencil
from Envelope import Envelope
from Scanner import Scanner
from Pen import Pen
from Printer import Printer
from Stapler import Stapler
from Form import Form
from Corrector import Corrector
from Ruler import Ruler
from Stamp import Stamp
from Monitor import Monitor
from Keybord import Keyboard
from Money_check_machine import Money_check_machine
from Cash_register import Cash_register


class Working_place:
    def __init__(self):
        self.chair = Chair("Офисный стул")
        self.table = Table("Рабочий стол")
        self.cabinet = Cabinet("Файловый шкаф")
        self.paper = Paper()
        self.pen = Pen()
        self.pencil = Pencil()
        self.stapler = Stapler()
        self.envelope = Envelope()
        self.form = Form()
        self.corrector = Corrector()
        self.ruler = Ruler()
        self.stamp = Stamp()
        self.printer = Printer()
        self.keyboard = Keyboard()
        self.monitor = Monitor()
        self.scanner = Scanner()
        self.money_check_machine = Money_check_machine()
        self.cash_register = Cash_register()

    def get_full_workplace_info(self):
        info = "=== ПОЛНАЯ ИНФОРМАЦИЯ О РАБОЧЕМ МЕСТЕ ===\n"
        info += f"Мебель: {self.chair.sit_on_chair()}, {self.table.info()}, {self.cabinet.store_items()}\n"
        info += f"Канцелярия: {self.pen.write('документ')}, {self.pencil.draw()}, {self.stapler.staple_papers()}\n"
        info += f"Техника: {self.printer.status()}, {self.scanner.check_status()}, {self.cash_register.cash_status()}\n"
        return info

