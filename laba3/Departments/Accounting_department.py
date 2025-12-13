from Departments.Department import Department

class Accounting_department(Department):
    def __init__(self, square, computers_count, safe_available):
        super().__init__(square)
        self.computers_count = computers_count
        self.safe_available = safe_available
        self._accountants = []

    def add_accountant(self, accountant):
        from Humans.Accountant import Accountant
        if isinstance(accountant, Accountant):
            self._accountants.append(accountant)
            accountant.set_department(self)
        else:
            print("Ошибка: можно добавить только объект класса Accountant")

    def get_accountants_count(self):
        return len(self._accountants)

    def list_accountants(self):
        return [acc.get_name() for acc in self._accountants]

    def has_safe(self):
        return self.safe_available