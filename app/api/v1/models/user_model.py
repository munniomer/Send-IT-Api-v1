users = []


class UserModel(object):
    """Class user models."""

    def __init__(self):
        self.db = users

    def add_user(self, fname, lname, email, phone, password, confirm_password, city):
        """ Method for saving user to the dictionary """
        payload = {
            "userId": len(self.db)+1,
            "fname": fname,
            "lname": lname,
            "email":  email,
            "phone":  phone,
            "password": password,
            "confirm_password": confirm_password,
            "city": city,
        }
        self.db.append(payload)
        return self.db

    def check_email(self, email):
        """Method for checking if user email exist"""
        user = [user for user in users if user['email'] == email]
        if user:
            return True
        return False

    def check_user(self, userId):
        """Method for checking if user exist"""
        user = [user for user in users if user['userId'] == userId]
        if user:
            return True
        return False

