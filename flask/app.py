from flask import Flask

# Connect to Redis
app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h1>Hello HKN!</h1>"
    return html 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
