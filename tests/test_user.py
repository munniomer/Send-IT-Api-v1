import unittest
from app import create_app
import json
from tests.basetest import BaseTest


class TestUSer(BaseTest):
    """User tests class"""

    def test_user_registration(self):
        "tests if new user can register"
        respon = self.client.post("/api/v1/user/register", json=self.new_user)
        self.assertEqual(respon.status_code, 201)

    def test_if_name_city_valid(self):
        """Tests if names and city are valid"""
        respon = self.client.post(
            "/api/v1/user/register", json=self.new_user1, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('PLease check if your fname, lname or city is empty or contains numbers',
                      str(respon.data))

    def test_if_email_valid(self):
        """Tests if email is valid"""
        respon = self.client.post(
            "/api/v1/user/register", json=self.new_user2, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please enter a valid emai',
                      str(respon.data))

    def test_if_email_exist(self):
        """Tests if email is valid"""
        self.client.post(
            "/api/v1/user/register", json=self.new_user6, content_type='application/json')
        respon = self.client.post(
            "/api/v1/user/register", json=self.new_user6, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('That email exists. use a unique email',
                      str(respon.data))

    def test_if_phone_valid(self):
        """Tests if email is exists"""
        respon = self.client.post(
            "/api/v1/user/register", json=self.new_user3, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please enter a valid phone number ',
                      str(respon.data))

    def test_if_password_valid(self):
        """Tests if passwords are empty or less than 3"""
        respon = self.client.post(
            "/api/v1/user/register", json=self.new_user4, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please check if your password or confirm password are empty or less than 3',
                      str(respon.data))

    def test_if_password_match(self):
        """Tests if passwords match"""
        respon = self.client.post(
            "/api/v1/user/register", json=self.new_user5, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('confirm password does not match password',
                      str(respon.data))
