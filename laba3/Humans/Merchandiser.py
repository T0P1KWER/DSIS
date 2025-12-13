from Humans.Internet_shop_worker import Internet_shop_worker

class Merchandiser(Internet_shop_worker):
    def __init__(self, name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                 work_experience, department, team_size):
        super().__init__(name, lastname, surname, age, gender, height, weight, worker_id, ownskills, education, status,
                         work_experience)
        self.__department = department
        self.__team_size = team_size
        self.__assigned_products = []

    def add_product(self, product):
        if hasattr(product, 'name') and product not in self.__assigned_products:
            self.__assigned_products.append(product)
            print(f"Товар '{product.name}' добавлен под контроль товароведа {self.name}")



    def get_products_count(self):
        return len(self.__assigned_products)