class Money_check_machine:

    def __init__(self):
        self.detection_method = "УФ"
        self.accuracy = 99.9
        self.supported_currencies = ["RUB", "USD", "EUR"]
    
    def check_bill(self, amount):
        return f"Купюра {amount} руб. проверена - подлинная"
    
    def detect_fake(self):
        return "Обнаружена поддельная купюра!"
    
    def get_supported_currencies(self):
        return f"Поддерживаемые валюты: {', '.join(self.supported_currencies)}"