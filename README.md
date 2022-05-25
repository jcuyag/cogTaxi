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


Populate database with NEW request using admin account. Execute this line multiple times as needed.
    
    http POST "http://165.22.101.120:8000/rides/admin/" "first_name"="Firstname" "last_name"="Lastname" "destination"="USA" "remarks"="good" "status"="new" "user_id"="00001"  -a  admin:admin


Get all bookings by an ADMIN

    http GET "http://165.22.101.120:8000/rides/" -a admin:admin


Get all bookings with NEW status from a registered driver. And select the request ID.

    http GET "http://165.22.101.120:8000/rides/" -a driver1:Sd9cCRcGhLuT2yQ


After getting the request ID to book. Use PUT method to update the status.

    http PUT "http://165.22.101.120:8000/rides/<ID>/" "status=booked" -a driver1:Sd9cCRcGhLuT2yQ


Get all Booked requests from a registered driver. (including DONE status)

    http GET "http://165.22.101.120:8000/rides/mybookings/" -a driver1:Sd9cCRcGhLuT2yQ
