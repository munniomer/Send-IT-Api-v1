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
        # check if the dh is empty
        if len(self.db) == 0:
            return {'message': 'There are no parcels created'}, 400
        return {'All parcel orders': self.db}, 200


    def get_specific_parcel(self, parcel_Id):
        """ Method for getting a specific parcel orders """
        parcel = [parcel for parcel in parcels if parcel['parcel_Id'] == parcel_Id]
        return parcel
