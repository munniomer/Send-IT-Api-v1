"""User views contains Signup and login Resources"""
from app.api.v1.models.parcels_model import ParcelModel
from app.api.v1.models.user_model import UserModel
from flask import Flask, request, make_response, json, jsonify
from flask_restful import Resource
from validators.validators import Validators

db = ParcelModel()
userobj = UserModel()
validate = Validators()


class ParcelResource(Resource):
    """Resource for user registration."""

    def post(self):
        """Method for posting user data"""
        request_data = request.get_json()
        print(request_data)
        sender_Id = request_data["sender_Id"]
        pickup_location = request_data["pickup_location"]
        destination = request_data["destination"]
        weight = request_data["weight"]
        quantity = request_data["quantity"]
        recipient_name = request_data["recipient_name"]
        recepient_phone = request_data["recepient_phone"]
        package_description = request_data["package_description"]

        # Check if user exists
        check_user = userobj.check_user(sender_Id)
        if not check_user:
            return {'msg': 'User doesnt exists! Create user first'}, 400

        # Check for Empty fields
        if pickup_location == "" or destination == "" or package_description == "":
            return {'message': "Please fill all the filds"}, 400

        # check if weight, quantity are string
        if isinstance(weight, str) or isinstance(quantity, str) or isinstance(recepient_phone, str):
            return {'message': "Make sure weight, quantity or recipient are numbers"}, 400

        # check if weight, quantity are 0 or negative
        if weight <= 0 or quantity <= 0 or recepient_phone <= 0:
            return {'message': "Make sure weight, quantity or phone are 0 or negative"}, 400

        # validate name
        if not validate.valid_name(recipient_name):
            return {'message': "recipient name cant be empty and should only contain letters "}, 400

        db.add_parcel(sender_Id, pickup_location, destination, weight,
                      quantity, recipient_name, recepient_phone, package_description)

        return {"message": "parcel delivery order successfully created", }, 201
