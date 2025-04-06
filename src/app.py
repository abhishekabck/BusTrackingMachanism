from flask import Flask, request, url_for, render_template
from html import escape

app = Flask(__name__, static_folder='static', template_folder='templates')



@app.route("/")
def index():
    return render_template("index.html", title="Home Page")

@app.route('/Login')
def login_menu():
    return render_template('LoginMenu.html')