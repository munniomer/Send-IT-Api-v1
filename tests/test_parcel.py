import unittest
from app import create_app
import json
from tests.basetest import BaseTest


class TestParcel(BaseTest):
    """Parcel tests class"""

    def test_parcel_creation(self):
        """tests if parcel can be created"""

        respon = self.client.post(
            "/api/v1/Parcels", json=self.new_parcel, content_type='application/json')
        self.assertEqual(respon.status_code, 201)
        self.assertIn(
            "parcel delivery order successfully created", str(respon.data))

    def test_if_argument_has_invalid_data(self):
        """Tests if a invalid data is provided"""
        respon = self.client.post(
            "/api/v1/Parcels", json=self.new_parcel3, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Make sure weight, quantity or recipient are numbers',
                      str(respon.data))

    def test_if_argument_is_provided(self):
        """Tests if there is empty fields"""
        respon = self.client.post(
            "/api/v1/Parcels", json=self.new_parcel4, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please fill all the filds',
                      str(respon.data))

    def test_recipient_name(self):
        """Tests if there is empty fields"""
        respon = self.client.post(
            "/api/v1/Parcels", json=self.new_parcel5, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('recipient name cant be empty and should only contain letters',
                      str(respon.data))

    def test_if_arguemnt_has_negative_values(self):
        """Tests if a negative value is provided"""
        respon = self.client.post(
            "/api/v1/Parcels", json=self.new_parcel2, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Make sure weight, quantity or phone are 0 or negative',
                      str(respon.data))

    def test_get_all_parcels(self):
        """Test to get all parcel delivery orders"""
        respon = self.client.get('/api/v1/Parcels/')
        return respon
