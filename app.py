#This is python file

import pandas as pd
import numpy as np 

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'default API'
    
