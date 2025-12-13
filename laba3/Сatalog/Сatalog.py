
class Catalog:
    def __init__(self):
        self.name = "Каталог 2025"
        self.content = []

    def add_product(self, product):
        if hasattr(product, 'name') and hasattr(product, 'price'):
            self.content.append(product)
            print(f"Товар '{product.name}' добавлен в каталог")
        else:
            print("Ошибка: объект не является товаром")

    def get_products_count(self):
        return len(self.content)

    def list_all_products(self):
        if not self.content:
            return "Каталог пуст"
        info = f"=== {self.name} ===\n"
        for i, product in enumerate(self.content, 1):
            info += f"{i}. {product.get_info()}\n"
        return info
    def sort_by_price(self):
        arr = self.content
        n = len(arr)
        left = 0
        right = n - 1
        while left < right:
            swapped = False
            for i in range(left, right):
                if arr[i].price > arr[i + 1].price:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            if not swapped:
                break
            right -= 1
            for i in range(right, left, -1):
                if arr[i].price < arr[i - 1].price:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    swapped = True
            if not swapped:
                break
            left += 1
        return self