from Сatalog.Product import Product
class Footwear(Product):
    def __init__(self, name, price, brand, in_stock, size, shoe_type, material):
        super().__init__(name, price, brand, in_stock)
        self.size = size                # Размер (например, 42)
        self.shoe_type = shoe_type      # "кроссовки", "ботинки", "сандалии"
        self.material = material        # "кожа", "текстиль"

    def try_on(self):
        return f"Примерка {self.shoe_type} размера {self.size}"