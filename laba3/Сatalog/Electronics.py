from Сatalog.Product import Product
class Electronics(Product):
    def __init__(self, name, price, brand, in_stock, warranty_months, power_watt=None):
        super().__init__(name, price, brand, in_stock)
        self.warranty_months = warranty_months  # Гарантия (месяцы)
        self.power_watt = power_watt            # Потребление (для техники)

    def get_warranty(self):
        return f"Гарантия: {self.warranty_months} мес."