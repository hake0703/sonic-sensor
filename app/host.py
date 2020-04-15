from flask import Flask
import sensor
from led import LED

app = Flask(__name__)
host_external = "0.0.0.0" # Allows app to be externally available
sense = sensor.SonicSensor()
light = LED(36)
_max_closed_distance = 10

@app.route("/")
def hello():
    return "Welcome to my garage...."

@app.route("/open")
def open():
    return "Garage Open and LED"

@app.route("/close")
def close():
    return "Garage Close... Bye, Bye."

@app.route("/testit")
def status():
    travel_time = sensor.get_signal_travel_time(sense)
    dist = sensor.get_distance_inches(travel_time)
    if dist < 10:
        light.trigger_led_on()
        return ("Distance = %.3f inches<br>LED Status: %s" % (dist, "on"))
    else:
        light.trigger_led_off()
        return ("Distance = %.3f inches<br>LED Status: %s" % (dist, "off"))

def garage_is_closed(distance):
    if distance <= _max_closed_distance:
        return True
    else:
        return False

if __name__ == "__main__":
    app.run(host=host_external)
