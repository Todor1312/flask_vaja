import requests

base_url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": "Kranj", "appid" : "ab9f79e7817ebddc0151c82d2e2eaf4b", "units" : "metric", "lang" : "sl"}

klic = requests.get(base_url, params = params).json()
#print(klic)

print("Občutek:", klic["main"]["feels_like"])
print("Vreme:", klic["weather"][0]["description"])
print("Oblaki:", klic["clouds"]["all"])