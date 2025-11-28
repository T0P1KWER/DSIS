class Form:
    def __init__(self):
        self.form_type = "заявление"
        self.fields_count = 5
        self.is_filled = False

    def fill_form(self):
        self.is_filled = True
        return f"Бланк {self.form_type} заполнен"