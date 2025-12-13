from Humans.Human import Human
import uuid
from datetime import datetime

# Импорты исключений
from Errors.Empty_email_error import Empty_email_error
from Errors.Invalid_phone_error import Invalid_phone_error
from Errors.Negative_price_error import Negative_price_error


class User(Human):
    def __init__(self, name, lastname, surname, age, gender, height, weight, email, phone):
        super().__init__(name, lastname, surname, age, gender, height, weight)
        self.__user_id = str(uuid.uuid4())[:8]
        self.__is_active = True
        self.__cart = []
        self.__wishlist = []
        self.__order_history = []
        self.__loyalty_points = 0
        self.__total_spent = 0.0
        self.__discount_level = "обычный"
        self.set_email(email)
        self.set_phone(phone)

    def get_user_id(self):
        return self.__user_id

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_loyalty_points(self):
        return self.__loyalty_points

    def get_total_spent(self):
        return self.__total_spent

    def get_discount_level(self):
        return self.__discount_level

    def get_cart_items_count(self):
        return len(self.__cart)

    def get_wishlist_items_count(self):
        return len(self.__wishlist)

    def get_orders_count(self):
        return len(self.__order_history)

    def set_email(self, new_email):
        try:
            if not new_email or not new_email.strip():
                raise empty_email_error("Email не может быть пустым!")
            if "@" not in new_email or "." not in new_email.split("@")[-1]:
                raise empty_email_error("Некорректный email адрес!")
            self.__email = new_email
            print(f"Email изменен на: {new_email}")
        except empty_email_error as e:
            print(f"Ошибка email: {e}")

    def set_phone(self, new_phone):
        try:
            cleaned = new_phone.replace("+", "").replace(" ", "").replace("-", "").strip()
            if not cleaned.isdigit() or len(cleaned) < 10:
                raise invalid_phone_error("Номер телефона должен содержать минимум 10 цифр!")
            self.__phone = new_phone
            print(f"Телефон изменен на: {new_phone}")
        except invalid_phone_error as e:
            print(f"Ошибка телефона: {e}")

    def set_total_spent(self, amount):
        try:
            if amount < 0:
                raise negative_price_error("Сумма покупок не может быть отрицательной!")
            self.__total_spent = float(amount)
            print(f"Общая сумма покупок установлена: {amount} руб.")
        except negative_price_error as e:
            print(f"Ошибка суммы: {e}")

    # === Остальные методы ===
    def get_user_info(self):
        info = [
            f"Пользователь: {self.lastname} {self.name} {self.surname}",
            f"ID: {self.__user_id}",
            f"Email: {self.__email}",
            f"Телефон: {self.__phone}",
            f"Уровень: {self.__discount_level}",
            f"Всего покупок: {self.__total_spent} руб.",
            f"Бонусные баллы: {self.__loyalty_points}",
            f"Заказов: {self.get_orders_count()}",
            f"В корзине: {self.get_cart_items_count()} товаров",
            f"В списке желаний: {self.get_wishlist_items_count()} товаров"
        ]
        return "\n".join(info)

    def deactivate_account(self):
        self.__is_active = False
        print("Аккаунт деактивирован")

    def is_active(self):
        return self.__is_active