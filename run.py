from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from ast import literal_eval
from PyCalculotron.components.calculation.fibonacci import fibonacci
from PyCalculotron.components.calculation.pythagore import pythagore
from PyCalculotron.components.calculation.bernouilli import experience as exp, print_bernouilli_result_array as bern

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'index.html',
        data={'title': 'index'}
    )


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


@app.route('/calculation/<operation>/<params>')
def calculation(operation, params):
    if operation == "fibonacci":
        assert params > 0
        result = fibonacci(params)
    elif operation == "bernouilli":
        assert "r" in params and "n" in params and params.r > 0 and params.n > 0
        experience = exp(params.n)
        bernouilli_array = bern(params.r, params.n)
        result = {"experience": experience, "bernouilli_array": bernouilli_array}
    elif operation == "pythagore":
        assert "a" in params and "b" in params and params.a > 0 and params.b > 0
        result = pythagore(params.a, params.b)

    return render_template("calculation.html", data={
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)
