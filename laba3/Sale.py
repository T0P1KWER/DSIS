class Sale:
    def __init__(self, discount_percent):
        self.discount_percent = discount_percent

    def apply_discount(self, original_price):
        discounted_price = original_price * (1 - self.discount_percent / 100)
        return round(discounted_price, 2)