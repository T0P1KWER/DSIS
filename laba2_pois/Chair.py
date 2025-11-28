from Furniture import Furniture
from SoBigWeight import SoBigWeight
class Chair(Furniture):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
        self.material = "дерево"
        self.legs_count = 4
        self.weight = 3
        self.price=500
        self.lifting_capacity=120
        self.easy_to_lifting_capacity=4

    def sit_on_chair(self):
        try:
            your_weight=input("Введите свой вес")
            your_weight=int(your_weight)
            if your_weight > self.lifting_capacity:
                raise   SoBigWeight("Стул не расчитан на таокй вес")
            return f"Сижу на  стуле"
        except SoBigWeight:
            return f"Ощибка: {SoBigWeight}"
