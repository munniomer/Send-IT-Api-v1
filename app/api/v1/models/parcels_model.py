parcels = []


class ParcelModel(object):
    """Class user models."""
    def __init__(self):
        """Initializes the parcel db"""
        self.db = parcels

    def add_parcel(self, sender_Id, pickup_location, destination, weight,
                   quantity, recipient_name, recepient_phone, package_description):
        """ Method for saving user to the dictionary """
        payload = {
            "parcel_Id": len(self.db)+1,
            "sender_Id": sender_Id,
            "pickup_location": pickup_location,
            "destination":  destination,
            "weight":  str(weight) + "kg",
            "quantity": quantity,
            "recipient_name": recipient_name,
            "recepient_phone": recepient_phone,
            "package_description": package_description,
            "status": "active",
            "current_location": pickup_location,
            "price": "Kshs." + str(float(weight) * 100)
        }
        self.db.append(payload)

    def get_all_parcels(self):
        """ Method for getting all available parcel orders """
        return self.db
     

    def get_specific_parcel(self, parcel_Id):
        """ Method for getting a specific parcel orders """
        parcel = [parcel for parcel in parcels if parcel['parcel_Id'] == parcel_Id]
        return parcel

    def update_parcel(self, parcel_Id):
        """ Method for canceling an order """
        for parcel in parcels:
            if parcel_Id == parcel["parcel_Id"]:
                parcel.update({"status": "Cancelled"})
                return parcel

    def get_user_orders(self,sender_Id):
        """ Method for fetching all orders for a specific user"""
        orders= [orders for orders in parcels if orders["sender_Id"]==sender_Id]
        return orders

