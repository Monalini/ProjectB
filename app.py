#This is python file

import pandas as pd
import numpy as np 

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'default API'


@app.route("/path")
def path_logic():
    return " Path API"


@app.route("predict",methods = ['GET,POST'])
def predict():
    #prediction logic
    return "API "



if __name__ == "__main__":
    app.run(debug = True)