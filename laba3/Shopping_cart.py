class Shopping_cart:
    def __init__(self):
        self.__items = []

    def add_item(self, product):
        if hasattr(product, 'name') and hasattr(product, 'price'):
            self.__items.append(product)
        else:
            print("Ошибка: можно добавлять только объекты Product")

    def remove_item(self, product):
        if product in self.__items:
            self.__items.remove(product)
        else:
            print("Товар не найден в корзине")

    def clear(self):
        self.__items.clear()



    def get_total_price(self):
        return sum(item.price for item in self.__items)

    def get_items_count(self):
        return len(self.__items)