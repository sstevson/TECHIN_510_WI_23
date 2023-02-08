# File: app2.py
# Author: David Stevson
# david@stevson.com
# 1/25/23
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Scott Stevson'))
