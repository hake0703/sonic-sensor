from flask import Flask
import sensor

app = Flask(__name__)
host_external = "0.0.0.0" # Allows app to be externally available
sense = sensor.SonicSensor()
_max_closed_distance = 10

@app.route("/")
def hello():
    return "Welcome to my garage...."

@app.route("/open")
def open():
    return "Garage Open!"

@app.route("/close")
def close():
    return "Garage Close... Bye, Bye."

@app.route("/status")
def status():
    travel_time = sensor.get_signal_travel_time(sense)
    dist = sensor.get_distance_inches(travel_time)
    return ("Distance = %.3f inches" % dist)

def garage_is_closed(distance):
    if distance <= _max_closed_distance:
        return True
    else:
        return False

if __name__ == "__main__":
    app.run(host=host_external)
