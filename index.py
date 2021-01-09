from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")

def index():
    return render_template("home.html")

@app.route("/sobre mi")
def contacto():
    return render_template("sobre mi.html")
    
@app.route("/Python")
def Python():
    return render_template("Python.html")

app.run(port=5000, debug = True)
