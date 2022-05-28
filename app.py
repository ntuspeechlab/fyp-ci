from flask import Flask
from pylint.utils import utils
app = Flask(__name__)

@app.route('/')
def hello_world():

    for i in [0,1,2,3,4,5]:
        print(i)
      
    return 'Hello, Docker!'
