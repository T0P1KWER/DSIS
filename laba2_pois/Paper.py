class Paper:
    def __init__(self):
        self.paper_type = "A4"
        self.quantity = 100
        self.color = "белый"

    def use_paper(self):
        return f"Использован лист {self.paper_type}"