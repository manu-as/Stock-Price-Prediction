from flask import Flask,render_template,request
from jinja2 import exceptions

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

@app.route("/login")
def login():
   return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)