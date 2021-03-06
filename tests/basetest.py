import unittest
from app import create_app
import json


class BaseTest(unittest.TestCase):
    """This is the test client"""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.new_user = {
            "fname": "Munira",
            "lname": "hadi",
            "email": "munira@gmail.com",
            "phone":  706335721,
            "password": "muni123",
            "confirm_password": "muni123",
            "city": "nairobi"
        }

        self.new_user1 = {
            "fname": "",
            "lname": "",
            "email": "muni@gmail.com",
            "phone":  70633578,
            "password": "muni123",
            "confirm_password": "muni123",
            "city": ""
        }

        self.new_user2 = {
            "fname": "Ali",
            "lname": "Abdi",
            "email": "muni",
            "phone":  70633578,
            "password": "muni123",
            "confirm_password": "muni123",
            "city": "Mombasa"
        }

        self.new_user3 = {
            "fname": "Muna",
            "lname": "Farah",
            "email": "munira@gmail.com",
            "phone":  "",
            "password": "muni123",
            "confirm_password": "muni123",
            "city": "Mombasa"
        }

        self.new_user4 = {
            "fname": "Muna",
            "lname": "Farah",
            "email": "munira@gmail.com",
            "phone":  706332571,
            "password": "",
            "confirm_password": "",
            "city": "Mombasa"
        }

        self.new_user5 = {
            "fname": "Muna",
            "lname": "Farah",
            "email": "munira@gmail.com",
            "phone":  706332571,
            "password": "muni",
            "confirm_password": "abc",
            "city": "Mombasa"
        }

        self.new_user6 = {
            "fname": "Muna",
            "lname": "Farah",
            "email": "abdi@gmail.com",
            "phone":  7063382571,
            "password": "muni",
            "confirm_password": "muni",
            "city": "Mombasa"
        }

        self.new_user7 = {
            "fname": "Muna",
            "lname": "Farah",
            "email": "abdi@gmail.com",
            "phone":  7063382571,
            "password": "muni",
            "confirm_password": "muni",
            "city": "Mombasa"
        }

        self.new_parcel = {
            "sender_Id": 1,
            "pickup_location": "Kisumu",
            "destination": "Nairobi",
            "weight": 3,
            "quantity": 1,
            "recipient_name": "Asha Omar",
            "recepient_phone": 706335721,
            "package_description": "Mobile phone"

        }

        self.new_parcel2 = {
            "sender_Id": 1,
            "pickup_location": "Kisumu",
            "destination": "Nairobi",
            "weight": 0,
            "quantity": -2,
            "recipient_name": "Asha Omar",
            "recepient_phone": -6,
            "package_description": "Mobile phone"

        }

        self.new_parcel3 = {
            "sender_Id": 1,
            "pickup_location": "Kisumu",
            "destination": "Nairobi",
            "weight": "",
            "quantity": "m",
            "recipient_name": "Asha Omar",
            "recepient_phone": "87",
            "package_description": "Mobile phone"

        }

        self.new_parcel4 = {
            "sender_Id": 1,
            "pickup_location": "",
            "destination": "",
            "weight": 3,
            "quantity": 1,
            "recipient_name": "Asha Omar",
            "recepient_phone": 706335721,
            "package_description": ""

        }

        self.new_parcel5 = {
            "sender_Id": 1,
            "pickup_location": "Kisumu",
            "destination": "Nairobi",
            "weight": 3,
            "quantity": 1,
            "recipient_name": "",
            "recepient_phone": 706335721,
            "package_description": "laptop"

        }

    def tearDown(self):
        """Destroys the test client when done"""
        self.app.testing = False
        self.app = None

    if __name__ == '__main__':
        unittest.main()
