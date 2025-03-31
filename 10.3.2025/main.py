import requests


def getJoke(tipSale):
    url = f"https://official-joke-api.appspot.com/jokes/{tipSale}/random"
    klic = requests.get(url).json()
    #print(klic)
    print(klic[0].get("setup", "Ni setupa"))
    print(klic[0].get("punchline", "Ni punchlinea"))
    print("*"*30)

getJoke("knock-knock")
getJoke("general")
getJoke("programming")
getJoke("dad")