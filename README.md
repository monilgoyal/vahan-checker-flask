# Vahan checker

Vahan checker can process the car image to extract registration number from license plate of car and fetch the details of owner and car with help of [regcheck](http://www.regcheck.org.uk/) api.

## Installation

Install all the required packages using file `requirements.txt`
```bash
pip install requirements.txt
```
###### Following libraries would be installed.
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [bs4](https://pypi.org/project/bs4/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [easyocr](https://pypi.org/project/easyocr/)
- [Flask](https://pypi.org/project/Flask/)
- [numpy](https://pypi.org/project/numpy/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [requests](https://pypi.org/project/requests/)

## Using Regcheck API
Create environmental variable `USER_NAME` or create a file in root directory with name `cred.env` and create variable `USER_NAME` and assign the username of regcheck account to it.

``` 
USER_NAME= #########
```

The following url is used to get the vehicle information.
http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber=plate_number&username=username
where `plate_number` is the value of extracted text from license plate image with help of easyocr and `username` is the username of regcheck Account.





