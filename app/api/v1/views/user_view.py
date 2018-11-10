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
        fname = request_data["fname"]
        lname = request_data["lname"]
        email = request_data["email"]
        phone = request_data["phone"]
        password = request_data["password"]
        confirm_password = request_data["confirm_password"]
        city = request_data["city"]

        if not validate.valid_name(fname):
            return {'message': "fname cant be empty and should only contain letters"}, 400
        
        if not validate.valid_name(lname):
            return {'message': "lname cant be empty and should only contain letters"}, 400
        
        if not validate.valid_email(email):
            return {'message': "please Enter a valid email"}, 400
        
        if not validate.valid_password(password):
            return {'message': "password cant be empty and not less than 3"}, 400

        if not validate.valid_name(city):
            return {'message': "please Enter a valid city"}, 400
        
        if not isinstance(phone,int):
            return {'message': "please Enter a valid phone number"}, 400

        db.add_user(fname, lname, email, phone, password, confirm_password,city)
        
        
        return {
        
            "message": "created successfully",
            "data" : db.__dict__
            }, 201

 