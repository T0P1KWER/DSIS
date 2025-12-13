from Сatalog.Product import Product
class UpperClothing(Product):
    def __init__(self, name, price, brand, in_stock, size, clothing_type, season):
        super().__init__(name, price, brand, in_stock)
        self.size = size                # "M", "L", 50 и т.д.
        self.clothing_type = clothing_type  # "куртка", "пальто", "ветровка"
        self.season = season            # "зима", "весна", "осень"

    def check_season(self):
        return f"{self.clothing_type} подходит для сезона: {self.season}"