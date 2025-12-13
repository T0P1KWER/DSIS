from Errors.Only_OSTIS_error import Only_OSTIS_error


class Recommend_system:
    def __init__(self, speed, accuracy, scalability, catalog_coverage):
        self.__speed = speed
        self.__accuracy = accuracy
        self.__scalability = scalability
        self.__catalog_coverage = catalog_coverage
        self.__technology = "OSTIS"

    def get_speed(self):
        return self.__speed
    def get_accuracy(self):
        return self.__accuracy

    def get_scalability(self):
        return self.__scalability

    def get_catalog_coverage(self):
        return self.__catalog_coverage

    def get_technology(self):
        return self.__technology
    def get_info(self):
        info = f"=== Рекомендательная система ===\n"
        info += f"Технология: {self.__technology}\n"
        info += f"Скорость: {self.__speed} мс\n"
        info += f"Точность: {self.__accuracy:.1f}%\n"
        info += f"Масштабируемость: до {self.__scalability:,} пользователей\n"
        info += f"Покрытие каталога: {self.__catalog_coverage:.1f}%\n"
        return info

    def set_technology(self, new_tech):
        try:
            self.__technology = new_tech
            if self.__technology != "OSTIS":
                raise Only_OSTIS_error("нужно использовать только остис")
            print(f"Технология обновлена на: {new_tech}")
        except Only_OSTIS_error:
            return f"Ощибка: {Only_OSTIS_error}"