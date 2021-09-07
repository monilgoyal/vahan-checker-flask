#!/usr/bin/env python
import os
import detect
from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from dotenv import load_dotenv
load_dotenv('cred.env')
app = Flask("myapp")


@ app.route("/", methods=['GET'])
def myhome():
    return render_template('home.html')


@ app.route("/", methods=['POST'])
def ajax():
    file = request.files['file'].read()
    npimg = np.frombuffer(file, dtype=np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    # return jsonify(status=0, carNumber="MH04JM8765", rtodata={'CarMake': {'CurrentTextValue': 'MAHINDRA AND MAHINDRA'}, 'CarModel': {'CurrentTextValue': 'E VERITO D6'}, 'Description': 'MAHINDRA AND MAHINDRA E VERITO D6', 'EngineNumber': 'K218D0163', 'EngineSize': {'CurrentTextValue': '0.0'}, 'Fitness': '-', 'FuelType': {'CurrentTextValue': 'ELECTRIC(BOV)'}, 'ImageUrl': 'http://www.carregistrationapi.in/image.aspx/@TUFISU5EUkEgQU5EIE1BSElORFJBIEUgVkVSSVRPIEQ2', 'Insurance': '2021-09-19', 'Location': 'RTO,THANE', 'MakeDescription': {'CurrentTextValue': 'MAHINDRA AND MAHINDRA'}, 'ModelDescription': {'CurrentTextValue': 'E VERITO D6'}, 'NumberOfSeats': {'CurrentTextValue': '5'}, 'Owner': 'INNOVATIONS FOR MANKIND', 'PUCC': '-', 'RegistrationDate': '17/10/2018', 'RegistrationYear': '2018', 'Variant': 'D6 (Electric)  1000.0', 'VechileIdentificationNumber': 'MA1LSEX79J2H80921', 'VehicleType': 'MOTOR CAR(LMV)'})
    return detect.plate_detect(img, os.getenv('USER_NAME'))


@ app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
