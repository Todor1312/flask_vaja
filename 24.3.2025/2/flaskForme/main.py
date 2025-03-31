from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getWeather")
def getWeather():
    kraj = request.args.get("kraj")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={kraj}&appid=ab9f79e7817ebddc0151c82d2e2eaf4b"
    return render_template("vreme.html", vreme = kraj)

app.run(debug = True)