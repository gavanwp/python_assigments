pi = 3.14159245
import requests
import json
city =input("Enter your city name")
url = f"{city}"
r = requests.get(url)
weather_json = json.loads(r)

print(weather_json)