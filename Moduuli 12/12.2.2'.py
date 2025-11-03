import json
import requests

city_name = input("Anna kaupungin nimi")
API_key = "d7fe370f07add1a168235c76ce632a28"

lang = "fi"
lat = ""
lng = ""

pyyntö = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_key}"

try:
    vastaus = requests.get(pyyntö)
    print("Status code: ", vastaus.status_code)
    if vastaus.status_code == 200:
        data = vastaus.json()
        print(json.dumps(data, indent=2))
        eka = data[0]
        print(eka)
        lat, lng = eka["lat"], eka["lng"]
        print(f"Kaupunki {city_name} leveysaste on: {lat} ja pituusaste on: {lng}")
except requests.exceptions.RequestException as e:
    print(e)
    print("Hakua ei voida suorittaa!")

pyyntö2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={API_key}"