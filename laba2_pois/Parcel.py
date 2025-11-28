class Parcel:
    def __init__(self, parcel_id, weight, sender, recipient):
        self.parcel_id = parcel_id
        self.weight = weight
        self.sender = sender
        self.recipient = recipient
        self.is_delivered = False

    def mark_delivered(self):
        self.is_delivered = True
        return f"Посылка {self.parcel_id} доставлена"