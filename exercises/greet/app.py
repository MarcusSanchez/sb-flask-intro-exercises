from flask import Flask

greet_app = Flask(__name__)


@greet_app.route('/welcome')
def welcome_route():
    return 'Welcome!'


@greet_app.route('/welcome/home')
def welcome_home_route():
    return 'Welcome home!'


@greet_app.route('/welcome/back')
def welcome_back_route():
    return 'Welcome back!'
