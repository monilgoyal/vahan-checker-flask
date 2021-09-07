import json
import re
import numpy as np
import cv2
import easyocr
from flask import jsonify
import requests
from bs4 import BeautifulSoup
plateCascade = cv2.CascadeClassifier('indian_license_plate.xml')
reader = easyocr.Reader(['en'])


def plate_detect(img, username):
    try:
        plateImg = img.copy()
        roi = img.copy()
        detected_no = 2
        minNbor = 1
        while detected_no > 1:
            plateRect = plateCascade.detectMultiScale(
                plateImg, scaleFactor=1.2, minNeighbors=minNbor)
            detected_no = plateRect.shape[0]
            minNbor += 1
        for (x, y, w, h) in plateRect:
            roi_ = roi[y:y+h, x:x+w, :]
            plate = roi[y:y+h, x:x+w, :]
            cv2.rectangle(plateImg, (x+2, y), (x+w-3, y+h-5), (0, 255, 0), 3)
        output = reader.readtext(plate)
        print(output)
        if len(output) == 1 and output[0][2] > .4:
            plate_number = ''.join(output[0][1].split(' ')).upper()
            plate_number = re.sub(r'[^\w]', '', plate_number)
            print(plate_number)
            if len(plate_number) == 10:
                url = f'http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={plate_number}&username={username}'
                data = BeautifulSoup(requests.get(
                    url).content, "xml").findAll(text=True)
                if len(data) != 0:
                    data = json.loads(data[1].replace("\n", ''))
                    return jsonify(status=0, carNumber=plate_number, rtodata=data)
                else:
                    return jsonify(status=1, rtodata={"type": "warning", "focus": "Sorry", "string": "Either number detected is wrong or not registered with RTO"})
            else:
                return jsonify(status=1, rtodata={"type": "danger", "focus": "Failed", "string": "Not able to detect RTO registration number inside image"})
        else:
            return jsonify(status=1, rtodata={"type": "danger", "focus": "Failed", "string": "Not able to detect RTO registration number inside image"})
    except:
        return jsonify(status=1, rtodata={"type": "danger", "focus": "Sorry", "string": "There is something wrong, try with different image"})
