from flask import Flask
app = Flask(__name__)

host_external = "0.0.0.0" # Allows app to be externally available

@app.route("/")
def hello():
    return "Welcome to my garage...."

@app.route("/open")
def open():
    return "Garage Open!"

@app.route("/close")
def close():
    return "Garage Close... Bye, Bye."

if __name__ == "__main__":
    app.run(host=host_external)
