from flask import Flask, render_template, request, redirect
from models import add_vehicle, get_vehicles

app = Flask(__name__)


@app.route("/")
def home():
    vehicles = get_vehicles()
    return render_template("index.html", vehicles=vehicles)


@app.route("/add_vehicle", methods=["POST"])
def add_vehicle_route():

    name = request.form["name"]
    number = request.form["number"]
    model = request.form["model"]
    status = request.form["status"]

    add_vehicle(name, number, model, status)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
