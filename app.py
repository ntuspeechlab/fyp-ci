from flask import Flask
from pylint.utils import utils
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'
