from flask import Flask, render_template, request
from PyCalculotron.components.calculation.fibonacci import fibonacci
from PyCalculotron.components.calculation.pythagore import pythagore
from PyCalculotron.components.calculation.bernouilli import experience as exp, bernouilli_result_array as bern
from PyCalculotron.components.conversion.conversion_dist import conversion_dist
from PyCalculotron.components.conversion.conversion_mass import conversion_mass
from PyCalculotron.components.conversion.conversion_temp import conversion_temp
from PyCalculotron.components.conversion.conversion_digit import conversion_digit


app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'index.html',
        data={'title': 'index'}
    )


@app.route('/conversion', methods=["GET", "POST"])
def conversion():
    if request.method == 'GET':
        return render_template("conversion.html", data={})

    elif request.method == 'POST':
        data = request.get_json()    

        selected_type = data['select-type']
        input = data['units-input']
        conv_type_in = data['type-in']
        conv_type_out = data['type-out']

        if selected_type == "masse":
            result = conversion_mass(input, conv_type_in, conv_type_out)
        elif selected_type == "temperature":
            result = conversion_temp(input, conv_type_in, conv_type_out)
        elif selected_type == "distance":
            result = conversion_dist(input, conv_type_in, conv_type_out)
        elif selected_type == "stockage":
            result = conversion_digit(input, conv_type_in, conv_type_out)

    return str(result)


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
            experience = exp(params[0])
            bernouilli_array = bern(params[1], params[0])
            result = {"Nombre de face": experience, "Nombre de face à chaque expérience": bernouilli_array}
        elif operator == "pythagore":
            assert len(params) == 2 and params[0] > 0 and params[1] > 0
            result = pythagore(params[0], params[1])

    return render_template("calculation.html", data={
        'operators': [{
            'operator': 'fibonacci',
            'params': ['Valeur à la position donnée']
        },
        {
            'operator': 'bernouilli',
            'params': ['Nombre de lancers de pièces', 'Nombre de fois où on répète l\'expérience']
        },
        {
            'operator': 'pythagore',
            'params': ['1er côté', '2nd côté']
        }],
        "result": result,
    })


if __name__ == "__main__":
    app.run(debug=True)
