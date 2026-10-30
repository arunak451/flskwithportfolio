from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello Flask!</h1>"

@app.route("/home")   
def home1():
    return "<h6>Welcome to Flask!</h6>" 


app.run(debug=True, port=5000)
