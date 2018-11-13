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
                "fname" : "Munira",
                "lname" : "hadi",
                "email" : "munira@gmail.com",
                "phone" :  706335721,
                "password" : "muni123",
                "confirm_password": "muni123",
                "city" : "nairobi"
        }
   
    def tearDown(self):
        """Destroys the test client when done"""
        self.app.testing = False
        self.app = None
    
    if __name__=='__main__':
        unittest.main()
