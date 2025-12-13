from Сatalog.Product import Product
class Cosmetics(Product):
    def __init__(self, name, price, brand, in_stock, volume_ml, is_natural):
        super().__init__(name, price, brand, in_stock)
        self.volume_ml = volume_ml
        self.is_natural = is_natural

    def describe(self):
        nature = "натуральный" if self.is_natural else "обычный"
        return f"{self.name} — {self.volume_ml} мл, {nature} состав"