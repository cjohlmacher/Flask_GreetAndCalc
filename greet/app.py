from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def greet():
    """General greet message"""
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    """Welcome home message"""
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
    """Welcome back message"""
    return 'welcome back'

