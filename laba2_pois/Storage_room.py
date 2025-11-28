from Room import Room
from TooManyShelvesError import TooManyShelvesError
class Storage_room(Room):
    def __init__(self, shelves_count, temperature, security_level, square):
        super().__init__(square)
        self.shelves_count = shelves_count
        self.temperature = temperature
        self.security_level = security_level

    def add_shelf(self):
        try:
            temp = input("Введите количество которое хотите добавить: ")
            shelf_to_add = int(temp)
            if shelf_to_add > 50:
                raise TooManyShelvesError("Нельзя добавить больше 50 за раз")
            self.shelves_count += shelf_to_add
            return f"Добавлено {shelf_to_add} полок. Теперь всего: {self.shelves_count}"
        except TooManyShelvesError :
            return f"Ошибка: {TooManyShelvesError}"
        except ValueError:
            return "Ошибка: нужно ввести число, а не текст!"