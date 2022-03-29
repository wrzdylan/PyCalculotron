from flask import Flask, session, render_template, redirect, request, url_for
import pandas as pd
import matplotlib.pyplot as plt
from ast import literal_eval

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html',
        data={'title' : 'index'}
    )

# @app.route('/theoremes')
# def theoremes():
#     return render_template(
#         'theoremes.html',
#         data={}
#     )

@app.route('/conversion')
def conversion():
    return render_template(
        'conversion.html',
        data={}
    )

@app.route('/calculatrice')
def calc():
    return render_template(
        'calculatrice.html',
        data={}
    )

@app.route('/equations')
def equations():
    return render_template(
        'equations.html',
        data={}
    )


if __name__ == "__main__":
    app.run(debug=True)