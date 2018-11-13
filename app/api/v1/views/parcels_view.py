"""Parcel views contains ParcelResource"""
from app.api.v1.models.parcels_model import ParcelModel
from flask import Flask, request, make_response, json, jsonify
from flask_restful import Resource
from validators.validators import Validators

db = ParcelModel()
validate = Validators()

class ParcelResource(Resource):
    """Resource for creating parcel orders."""

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

        db.add_parcel(sender_Id, pickup_location, destination, weight,
                      quantity, recipient_name, recepient_phone, package_description)

        return {"message": "created successfully"}, 201
