import unittest
from app import create_app
import json
from tests.basetest import BaseTest


class TestParcel(BaseTest):
    """Parcel tests class"""

    def test_parcel_creation(self):
        """tests if parcel can be created"""
        self.client.post("/api/v1/user/register", json=self.new_user6)
        respon = self.client.post(
            "/api/v1/parcels", json=self.new_parcel, content_type='application/json')
        self.assertEqual(respon.status_code, 201)
        self.assertIn(
            "parcel delivery order successfully created", str(respon.data))

    def test_if_argument_has_invalid_data(self):
        """Tests if a invalid data is provided"""
        self.client.post("/api/v1/user/register", json=self.new_user6)
        respon = self.client.post(
            "/api/v1/parcels", json=self.new_parcel3, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Make sure weight, quantity or recipient are numbers',
                      str(respon.data))

    def test_if_argument_is_provided(self):
        """Tests if there is empty fields"""
        self.client.post("/api/v1/user/register", json=self.new_user6)
        respon = self.client.post(
            "/api/v1/parcels", json=self.new_parcel4, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Please fill all the filds',
                      str(respon.data))

    def test_recipient_name(self):
        """Tests if there is empty fields"""
        self.client.post("/api/v1/user/register", json=self.new_user6)
        respon = self.client.post(
            "/api/v1/parcels", json=self.new_parcel5, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('recipient name cant be empty and should only contain letters',
                      str(respon.data))

    def test_if_arguemnt_has_negative_values(self):
        """Tests if a negative value is provided"""
        self.client.post("/api/v1/user/register", json=self.new_user6)
        respon = self.client.post(
            "/api/v1/parcels", json=self.new_parcel2, content_type='application/json')
        self.assertEqual(respon.status_code, 400)
        self.assertIn('Make sure weight, quantity or phone are 0 or negative',
                      str(respon.data))

    def test_get_all_parcels(self):
        """Test to get all parcel delivery orders"""
        self.client.post("/api/v1/user/register", json=self.new_user6)
        self.client.post(
            "/api/v1/parcels", json=self.new_parcel, content_type='application/json')
        respon = self.client.get('/api/v1/parcels')
        self.assertEqual(respon.status_code, 200)

    def test_to_get_all_parcels(self):
        """Test when no parcels are there to fetch"""
        respon = self.client.get('/api/v1/parcels/')
        self.assertEqual(respon.status_code, 200)

    def test_get_specific_parcel(self):
        """Test to fetch a specific parcel order"""
        self.client.post(
            "/api/v1/parcels", json=self.new_parcel, content_type='application/json')
        respon = self.client.get('/api/v1/parcels/1')
        self.assertEqual(respon.status_code, 200)

    def test_for_get_specific_parcel(self):
        """Test when a specific parcel does not exist"""
        self.client.post(
            "/api/v1/parcels", json=self.new_parcel, content_type='application/json')
        respon = self.client.get('/api/v1/parcels/1000')
        self.assertEqual(respon.status_code, 404)

    def test_for_update_parcel(self):
        """Test for canceling the order that doesnt exist"""
        self.client.post("/api/v1/user/register", json=self.new_user6)
        self.client.post(
            "/api/v1/parcels", json=self.new_parcel, content_type='application/json')
        self.client.put(
            "/api/v1/parcels", json=self.new_parcel, content_type='application/json')
        respon = self.client.get('/api/v1/parcels/1/cancel')
        self.assertEqual(respon.status_code, 200)

    def test_update_parcel(self):
        """Test for canceling the order that doesnt exist"""
        respon = self.client.get('/api/v1/parcels/100/cancel')
        self.assertEqual(respon.status_code, 404)

    def test_user_order(self):
        """Test for fetcing specific user orders"""
        self.client.post("/api/v1/user/register", json=self.new_user6)
        self.client.post(
            "/api/v1/parcels", json=self.new_parcel, content_type='application/json')
        respon = self.client.get('/api/v1/users/1/parcels')
        self.assertEqual(respon.status_code, 200)

    def test_for_user_order(self):
        """Test for fetcing specific user orders that doesnt exists"""
        self.client.post("/api/v1/user/register", json=self.new_user6)
        self.client.post(
            "/api/v1/parcels", json=self.new_parcel, content_type='application/json')
        respon = self.client.get('/api/v1/users/100/parcels')
        self.assertEqual(respon.status_code, 404)
