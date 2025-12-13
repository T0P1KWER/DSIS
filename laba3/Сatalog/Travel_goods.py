
from Сatalog.Product import Product
class TravelGoods(Product):
    def __init__(self, name, price, brand, in_stock, weight_kg, waterproof):
        super().__init__(name, price, brand, in_stock)
        self.weight_kg = weight_kg
        self.waterproof = waterproof

