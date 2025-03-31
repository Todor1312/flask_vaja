from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def indeks():
    return render_template("indeks.html")

@app.route("/chuck")
def chuck():
    url = "https://api.breakingbadquotes.xyz/v1/quotes"
    klic = requests.get(url).json()
    avtor = klic[0]["author"]
    joke = klic[0]["quote"]
    return render_template("chuck.html", vic = joke, kreator = avtor)


app.run(debug=True)