import csv
import pandas as pd
from sqlalchemy import create_engine
import sqlite3
from flask import Flask, request, render_template, jsonify
from sqlalchemy.orm import Session 

from flask import Flask, render_template 
import subprocess 

app = Flask(__name__) 
    
@app.route('/') 

def index(): 
    #Convert the Jupyter notebook to Voilà application 
    subprocess.Popen(['voila', 'loan_prediction.ipynb', '--no-browser']) 
    return render_template('index.html') 

if __name__ == '__main__': 
    app.run(debug=True) 
