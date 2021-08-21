# import flask
from flask import Flask

# create a new Flask app instance
app = Flask(__name__)

# create flask routes
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/')
def my_gf():
    return 'My beautiful girlfriend: Zoe!'