from flask import Flask, render_template

# instance of flask application
app = Flask(__name__)

@app.route("/")
def home_index():
    return render_template('home/index.html')

@app.route("/security/login")
def home_login():
    return render_template('home/login.html')