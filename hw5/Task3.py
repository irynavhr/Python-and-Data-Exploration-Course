# developed by Iryna Hrytsenko

import requests
import json

# get input coordinates
latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")

# creat url
url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"

# header
headers = {
    "User-Agent": "MyGeocoderApp/1.0 (your_email@example.com)"
}

# request
response = requests.get(url, headers=headers)

# check
if response.status_code != 200:
    print("Error fetching data from the API.")
    quit()

# parse
data = response.json()

# extract
print("\nReverse Geocoding Result:")
address = data.get("address", {})
display_name = data.get("display_name", "Unknown")
place_type = data.get("type", "Unknown")
house_number = address.get("house_number", "N/A")
road = address.get("road", "N/A")
city = address.get("city", address.get("town", address.get("village", "N/A")))
postcode = address.get("postcode", "N/A")
country = address.get("country", "Unknown")
country_code = address.get("country_code", "Unknown")

# print
print(f"Place name      : {display_name}")
print(f"Place type      : {place_type}")
print(f"House number    : {house_number}")
print(f"Street          : {road}")
print(f"City            : {city}")
print(f"Postcode        : {postcode}")
print(f"Country         : {country}")
print(f"Country code    : {country_code.upper()}")
