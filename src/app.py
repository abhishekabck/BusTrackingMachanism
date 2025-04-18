from flask import Flask, request, url_for, render_template
from html import escape

app = Flask(__name__, static_folder='statics', template_folder='templates')



@app.route("/")
def index():
    return render_template("index.html", title="Home Page")

@app.route('/Login')
def login_menu():
    return render_template('LoginMenu.html', title="Login | College BusTracker ")

@app.route('/SignUp')
def signup_menu():
    return render_template('SignUpMenu.html', title="SignUp | College BusTracker ")

@app.route('/student-signup')
def student_signup():
    return render_template('SignUpStudent.html', title="SignUp | Student | College BusTracker ")
