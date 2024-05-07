import requests

BEARER = "BYJGNuhmhuhkuhmknGGgmnjnhhnmjng"
PROJECT = "flightDeals"
SHEET = "users"
FLIGHT_DEALS_USERS = "https://api.sheety.co/f34ae5bff87e0200b3b4b3eef4f978de/flightDeals/users"


def post_new_row(first_name, last_name, email):
    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
    }

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=FLIGHT_DEALS_USERS, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)
