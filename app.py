
# Importing Flask
from flask import Flask

# Creating a new flask app Instance
app = Flask(__name__)

# Creating a route
@app.route('/')
def hello_world():
    return 'Hello world'
