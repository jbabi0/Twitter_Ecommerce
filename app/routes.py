# import necessary functions and classes

from app import app
from flask import render_template, url_for, redirect

# create page routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
