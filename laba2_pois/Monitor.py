class Monitor:
    def __init__(self):
        self.screen_size = 24
        self.resolution = "1920x1080"
        self.brightness = 80
    
    def display_info(self, info):
        return f"На экране отображается: {info}"