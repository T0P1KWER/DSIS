class Cash_register:
    def __init__(self):
        self.cash_amount = 10000
        self.receipt_number = 1
        self.is_open = True
    
    def process_payment(self, amount):
        self.cash_amount += amount
        self.receipt_number += 1
        return f"Оплата {amount} руб. принята. Чек №{self.receipt_number}"
    
    def print_receipt(self):
        return f"Чек №{self.receipt_number} напечатан"
    
    def cash_status(self):
        return f"В кассе: {self.cash_amount} руб."