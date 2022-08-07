# Import the Flask Dependency
from flask import Flask 

# Create a Flask instance (A singular version of something)
app = Flask(__name__)

# Create a Flask route
@app.route('/')
def hello_world():
    return 'Hello World'

