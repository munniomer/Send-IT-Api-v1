"""User views contains Signup and login Resources"""

from app.api.v1.models.user_model import UserModel
from flask import Flask, request, make_response,json,jsonify
import json
from flask_restful import Resource
from validators.validators import Validators

db = UserModel()
validate = Validators()

class SignupResource(Resource):
    """Resource for user registration."""

    def post(self):
        """Method for posting user data"""
        request_data = request.get_json()
        print(request_data)
        fname = request_data["fname"]
        lname = request_data["lname"]
        email = request_data["email"]
        phone = request_data["phone"]
        password = request_data["password"]
        confirm_password = request_data["confirm_password"]
        city = request_data["city"]

        db.add_user(fname, lname, email, phone, password, confirm_password,city)
        
        
        return {
        
            "message": "created successfully",
            "data" : db.__dict__
            }, 201

 