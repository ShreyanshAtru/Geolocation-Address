# Geolocation-Address-
API created for getting longitude and latitude from a address 

1. Create virtualenv and run the requirement.txt file 
2. after that go to the project directry and then in origin_api/services.py and add you "API_KEY"
    API_KEY = your_key
3. for run the project go to the project directory and run -->
    py manage.py runserver 

## API Uses 
url/localhost : http://127.0.0.1:8000/address

4. API body take input as 
    {"address": "your address",
      "putput_format":"json or xml"}

