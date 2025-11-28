class Book_of_complains:
    def __init__(self, complaints_count, pages_count, location):
        self.complaints_count = complaints_count
        self.pages_count = pages_count
        self.location = location

    def add_complaint(self):
        return "Жалоба добавлена в книгу"