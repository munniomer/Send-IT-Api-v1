"""User views contains Signup and login Resources"""
from app.api.v1.models.user_model import UserModel
from flask import Flask, request, make_response, json, jsonify
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

        # Checks if names and city are valid
        if not validate.valid_name(fname) or not validate.valid_name(lname) or not validate.valid_name(city):
            return {'message': "PLease check if your fname, lname or city is empty or contains numbers"}, 400

        # Checks if email is valid
        if not validate.valid_email(email):
            return {'message': "Please enter a valid email "}, 400

        # checks if email exists
        check_email = db.check_email(email)
        if check_email:
            return {'message': 'That email exists. use a unique email'}, 400

        # Checks if phone is valid
        if not isinstance(phone, int):
            return {'message': "Please enter a valid phone number "}, 400

        # Checks if passwords are empty or less than 3
        if not validate.valid_password(password) or not validate.valid_password(confirm_password):
            return {'message': "Please check if your password or confirm password are empty or less than 3"}, 400

        # checks if confirm password is equal to password
        if confirm_password != password:
            return {"message": "confirm password does not match password"},400

        data=db.add_user(fname, lname, email, phone,
                    password, confirm_password, city)

        return {"All users": data,
            "message": "User successfully created", }, 201
