from Bilding import Bilding


class Post_office(Bilding):
    def __init__(self, address, tipe, date_of_building, square, number_of_storeys, price, working_grafic):
        super().__init__(address, tipe, date_of_building, square, number_of_storeys)
        self.__price = price
        self.working_grafic = working_grafic
        self.__working_status = "working"
        self.__count_of_postman = 0
        self.__postmen = []

    def add_postman(self, postman):
        if postman not in self.__postmen:
            self.__postmen.append(postman)
            self.__count_of_postman += 1
            print(f"Почтальон {postman.lastname} добавлен в офис")

    def remove_postman(self, postman):
        if postman in self.__postmen:
            self.__postmen.remove(postman)
            self.__count_of_postman -= 1
            print(f"Почтальон {postman.lastname} удален из офиса")

    def get_postmen_count(self):
        return self.__count_of_postman

    def get_postmen_list(self):
        return self.__postmen

    def rebuilding(self):
        print("rebuilding")

    def sell_office(self):
        print(f"office was selled for {self.__price}")
        self.__working_status = "dont work"
        self.__price = 0