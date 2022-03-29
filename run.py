from flask import Flask, render_template
from PyCalculotron.components.calculation.fibonacci import fibonacci
from PyCalculotron.components.calculation.bernouilli import experience as exp, print_bernouilli_result_array as bern

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world !"


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

    return render_template("calculation.html", data={
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)
