from Сatalog.Product import Product
class Toys(Product):
    def __init__(self, name, price, brand, in_stock, age_from, is_educational):
        super().__init__(name, price, brand, in_stock)
        self.age_from = age_from            # Возраст от (лет)
        self.is_educational = is_educational  # Развивающая?

    def recommend_age(self):
        return f"Рекомендуется с {self.age_from} лет"