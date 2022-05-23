This code utilizes `Python 3.8` and `Django Rest Framework` for the API development 


Installation
------------
Clone this project and install the requirements.txt via pip command.
    
    pip install -r requirements.txt


HTTPie command-line HTTP client tool for testing the API via CLI interaction

     apt install httpie 


Usage
-----
Registered drivers in the deployed server credentials.

    driver1:Password123

    driver2:Password123


Create new booking request for registered driver (POST)
`http POST`

Get all bookings with NEW status from registered driver (GET)
`http GET`

