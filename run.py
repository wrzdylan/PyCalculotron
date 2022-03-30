from flask import Flask, render_template, request
from PyCalculotron.components.calculation.fibonacci import fibonacci
from PyCalculotron.components.calculation.pythagore import pythagore
from PyCalculotron.components.calculation.bernouilli import experience as exp, bernouilli_result_array as bern

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


@app.route('/calculotron', methods=["GET", "POST"])
def calculotron():
    if request.method == "GET":
        result = None
    elif request.method == "POST":
        operator = request.form['operator']

        params = [int(request.form[name]) for name in request.form if name.split("-")[0] == operator]

        if operator == "fibonacci":
            assert params[0] > 0
            result = fibonacci(params[0])
        elif operator == "bernouilli":
            assert len(params) == 2 and params[0] > 0 and params[1] > 0
            experience = exp(params[1])
            bernouilli_array = bern(params[0], params[1])
            result = {"experience": experience, "bernouilli_array": bernouilli_array}
        elif operator == "pythagore":
            assert len(params) == 2 and params[0] > 0 and params[1] > 0
            result = pythagore(params[0], params[1])

    return render_template("calculation.html", data={
        'operators': [{
            'operator': 'fibonacci',
            'params': ['x']
        },
        {
            'operator': 'bernouilli',
            'params': ['r', 'n']
        },
        {
            'operator': 'pythagore',
            'params': ['a', 'b']
        }],
        "result": result,
    })


if __name__ == "__main__":
    app.run(debug=True)
