from Сatalog.Product import Product
class LowerClothing(Product):
    def __init__(self, name, price, brand, in_stock, size, clothing_type, color):
        super().__init__(name, price, brand, in_stock)
        self.size = size
        self.clothing_type = clothing_type  # "джинсы", "шорты", "брюки"
        self.color = color

    def match_with_upper(self, upper_item):
        return f"{self.name} можно сочетать с {upper_item.name}"