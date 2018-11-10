"""User views contains Signup and login Resources"""

from app.api.v1.models.user_model import UserModel
from flask import Flask, request, jsonify, make_response, json
from flask_restful import Resource

db = UserModel()

class SignupResource(Resource):
    """Resource for user registration."""
   
    def post(self):
        """Method for posting user data"""
        data = request.get_json()
        fname = data["fname"]
        lname = data["lname"]
        email = data["email"]
        phone = data["phone"]
        password = data["password"]
        city = data["city"]

        db.add_user(fname, lname, email, phone, password, city)
        
        return {"message": "created successfully"}, 201

 