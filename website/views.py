
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

   return render_template('index.html',
                           title='Home')

@app.route('/provisions')
def provisions():
    return render_template('provisions.html',
                           title='Provisions')


