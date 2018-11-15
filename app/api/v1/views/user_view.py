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

        if not validate.valid_name(fname):
            return {'message': "first name cant be empty and should only contain letters "}, 400

        if not validate.valid_name(lname):
            return {'message': "last name cant be empty and should only contain letters "}, 400

        if not validate.valid_email(email):
            return {'message': "Please enter a valid email "}, 400

        if not isinstance(phone, int):
            return {'message': "Please enter a valid phone number "}, 400

        if not validate.valid_password(password):
            return {'message': "passowrd cannot be less than 3"}, 400

        if not validate.valid_password(confirm_password):
            return {'message': "confirm passowrd cannot be less than 3"}, 400

        if confirm_password != password:
            return {"message": "confirm password does not match password"}

        if not validate.valid_name(city):
            return {'message': "City cant be empty and should only contain letters "}, 400

        check_email = db.check_email(email)
        if check_email:
            return {'message': 'That email exists. use a unique email'}, 400

        db.add_user(fname, lname, email, phone,
                    password, confirm_password, city)

        return {
            "message": "User successfully created", }, 201

    def get(self):
        """Method for fetching all users"""
        users = db.get_all_user()
        return users

