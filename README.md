# Send-IT

Send-IT is a courier service Application that helps users deliver parcels to different destinations. Send-IT provides courier quotes based on weight categories.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/munniomer/Send-IT-Api-v1.svg?branch=ft-cancel-order-v1-161985069)](https://travis-ci.com/munniomer/Send-IT-Api-v1)
[![Coverage Status](https://coveralls.io/repos/github/munniomer/Send-IT-Api-v1/badge.svg?branch=ft-cancel-order-v1-161985069)](https://coveralls.io/github/munniomer/Send-IT-Api-v1?branch=ft-cancel-order-v1-161985069)

## The required API Endpoints that enable one:
 1. Create a parcel delivery order
 2. Get all parcel delivery orders
 3. Get a specific parcel delivery order
 4. Cancel a parcel delivery order
 5. Get all parcel delivery orders by a specific user
 
 ## The list of the functioning API Endpoints

Method        | EndPoint      | Functionality |
------------- | ------------- | ---------------
POST  | api/v1/user/registter  | Creates a user   |
POST  | api/v1/parcels  | Create a parcel delivery order   |
GET  | /api/v1/parcel  | Gets all parcel delivery orders   |
GET  | /api/v1/parcel/<parcelid>  | Get a specific parcel delivery order   
PUT  | /api/v1/parcels/<parcelId>/cancel | Cancel the specific parcel delivery order   |
GET  | /api/v1/users/<userId>/parcels| Fetch all parcel delivery orders by a specific user   |
  
  
## Installation
Make sure you have Python3 installed on your machine
  - Start by creating a directory on your machine and Switch to the directory you created
 ```bash
$ mkdir Send-IT-Api-v1
$ cd Send-IT-Api-v1
```
- Install git in your directory
 ```bash
$ git init
```
- Clone this repo Switch to it
 ```bash
$ git clone https://github.com/munniomer/Send-IT-Api-v1.git 
$ cd Send-IT-Api-v1
```
- Install a virtual Environment and activate it
 ```bash
$ python -m venv venv 	
$ source venv/bin/activate
```
- Install the dependencies using the requirements file
 ```bash
$ pip install -r requirements.txt
```
- Run the app
 ```bash
$ export FLASK_ENV=development
$ export FLASK_APP=run.py
$ flask run
```
## Testing the endpoints
- Install postman to test the endpoints 

- Open postman and navigate to the localhost and add the enpoint route you are testing
 ```bash
 http://localhost:5000/api/v1/<endpoint>
 
```
## Running tests
To Run the tests you have to use the terminal, switch to the project folder and activate the venv.

- To check if all tests pass
```bash
$ pytest 
```
- To check the test Coverage 

```bash
$ pytest --cov app  
```

## Technologies used
- Python 3.6
- Flask framework
- Unittest for testing

## Author: Munira Omar

__Copyright © Andela 2018__



