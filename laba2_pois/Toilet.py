from Room import Room
class Toilet(Room):
    def __init__(self, square, cabins_count, has_mirror):
        super().__init__(square)
        self.cabins_count = cabins_count
        self.has_mirror = has_mirror


    def get_toilet_info(self):
        return f"Туалет: {self.square} м², кабинок: {self.cabins_count}"
