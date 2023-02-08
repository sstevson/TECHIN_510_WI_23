# File: app3.py
# Author: David Stevson
# david@stevson.com
# 1/27/23

from flask import Flask, request, make_response, redirect

app = Flask(__name__)


# what visitors see when requesting the main page
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is {}.</h1>'.format(user_agent)


# what specific users see when requesting /user
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


# add a 400 response to a bad route
@app.route('/bad-route')
def bad_route():
    return '<h1>Bad Request</h1>', 400


# drop a cookie bomb on the user
@app.route('/cookie')
def cookie_monster():
    response = make_response('<h1>This page carries a cookie. Enjoy!</h1>')
    response.set_cookie('answer', '42')
    return response


# redirect user to the Flask project
@app.route('/flask')
def go_to_flask():
    return redirect('https://palletsprojects.com/p/flask/')


# Using a text string without HTML
@app.route('/text')
def text():
    return 'This is some text.'


if __name__ == '__main__':
    app.run()
