import unittest
from app import create_app
import json
from tests.basetest import BaseTest

class TestUSer(BaseTest):
     """User tests class"""
     
     def test_user_registration(self):
        "tests if new user can register"

        respon = self.client.post("/api/v1/user/register", json=self.new_user)
        self.assertEqual(respon.status_code,201)
       



