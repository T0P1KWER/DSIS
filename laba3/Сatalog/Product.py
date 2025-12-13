class Product:
    def __init__(self, name, price, brand, in_stock):
        self.name = name
        self.price = price
        self.brand = brand
        self.in_stock = in_stock

    def get_info(self):
        return f"{self.name} ({self.brand}) — {self.price} руб."

    def is_available(self):
        return self.in_stock