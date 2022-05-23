This code utilizes `Python 3.8` and `Django Rest Framework` for the API development 


Installation
------------
Clone this project and install the requirements.txt via pip command.
    
    pip install -r requirements.txt

Run migration. 

    ./manage.py makemigrations
    ./manage.py migrate

Start the server.

    ./manage.py runserver

Install HTTPie command-line HTTP client tool for testing the API via CLI interaction

     apt install httpie 


Usage
-----
Registered drivers in the deployed server credentials.

    admin:admin

    driver1:Sd9cCRcGhLuT2yQ

    driver2:Sd9cCRcGhLuT2yQ


Create new booking request for registered driver (POST)
    
    http POST "165.22.101.120:8000/rides/driver/" "first_name"="Firstname" "last_name"="Lastname" "destination"="USA" "remarks"="good" "status"="new" "user_id"="0000driver2"  -a  driver1:Sd9cCRcGhLuT2yQ

Get all bookings with NEW status from registered driver (GET)

    http GET "165.22.101.120:8000/rides/driver/" -a driver1:Sd9cCRcGhLuT2yQ

Get all bookings by an ADMIN

    http GET "165.22.101.120:8000/rides/admin/" -a admin:admin
