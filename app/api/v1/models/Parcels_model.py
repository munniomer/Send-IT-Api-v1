from datetime import datetime
Parcels = []

class ParcelModel(object):
    """Class Parcel models."""
    def __init__(self):
      """ initializes the parcel db"""
      self.db = Parcels 

    def add_parcel(self,sender_Id,pickup_location,destination,weight,recipient_name,recepient_phone,package_description):
        """ Method for saving new orders to the dictionary """
        payload = {
            "parcelId": len(self.db)+1,
            "sender_Id" : sender_Id,
            "pickup_location" : pickup_location,
            "destination" :  destination,
            "weight":  str(weight) + "kg",
            "recipient_name": recipient_name,
            "recepient_phone": recepient_phone,
            "package_description": package_description,
            "status": "in-transit",
            "current_location": pickup_location,
            "sent_date": datetime.now,
            "price": "Kshs." + str(float(weight) * 10)
        }
        self.db.append(payload)