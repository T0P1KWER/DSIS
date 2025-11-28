from Furniture import Furniture
class Cabinet(Furniture):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
        self.shelves = 5
        self.color = "бежевый"
        self.weight = 9
        self.price = 560

    def store_items(self):
        return f"Предметы хранятся в {self.color} шкафу"