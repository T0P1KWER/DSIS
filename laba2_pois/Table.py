from Furniture import Furniture


class Table(Furniture):
    def __init__(self, name):
        super().__init__(name )
        self.name = name
        self.height = 75
        self.shape = "прямоугольный"
        self.weight = 23
        self.price = 533
        self.legs_count = 4

    def info(self):
        return f"Стол: {self.name}, высота: {self.height}см, форма: {self.shape}, вес: {self.weight}кг, цена: {self.price}руб, ножек: {self.legs_count}"