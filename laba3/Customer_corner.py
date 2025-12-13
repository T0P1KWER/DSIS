class Customer_corner:
    def __init__(self, brochures_count, information_stands, feedback_box):
        self.brochures_count = brochures_count
        self.information_stands = information_stands
        self.feedback_box = feedback_box

    def provide_information(self):
        return "Информация предоставлена потребителю"