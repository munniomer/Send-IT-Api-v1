from flask import Flask, Blueprint
from flask_restful import Api, Resource 
from app.api.v1.views.user_view import SignupResource
from app.api.v1.views.parcels_view import ParcelResource

v1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
app = Api(v1)  

#Resources are the spiecific route we need to pass the endpoint

# Users
app.add_resource(SignupResource, '/user/register')

# Parcels
app.add_resource(ParcelResource, '/Parcels')

