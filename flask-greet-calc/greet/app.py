from flask import Flask, request

app = Flask (__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome'

@app.route('/welcome/home')
def welcomehome():
    return 'Welcome home'

@app.route('/welcome/back')
def welcomeback():
    return 'Welcome back'