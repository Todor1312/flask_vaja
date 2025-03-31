from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "test"#render_template("index.html")

@app.route("/getWeather")
def getWeather():
    kraj = #print #(request.args.get("kraj"))
    #API weather 
    #Temperatura, padavine...

return render_template("vreme.html", vreme = kraj)

app.run(debug = True)
