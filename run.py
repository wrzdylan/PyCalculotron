from flask import Flask, render_template, request
from PyCalculotron.components.calculation.fibonacci import fibonacci
from PyCalculotron.components.calculation.pythagore import pythagore
from PyCalculotron.components.calculation.bernouilli import experience as exp, bernouilli_result_array as bern
from PyCalculotron.components.conversion.conversion_dist import conversion_dist
from PyCalculotron.components.conversion.conversion_mass import conversion_mass
from PyCalculotron.components.conversion.conversion_temp import conversion_temp
from PyCalculotron.components.conversion.conversion_digit import conversion_digit
from PyCalculotron.components.conversion.conversion_energy import conversion_energy
from PyCalculotron.components.conversion.conversion_vit import conversion_vit
from PyCalculotron.components.conversion.conversion_vol import conversion_vol


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
        elif selected_type == "energie":
            result = conversion_energy(input, conv_type_in, conv_type_out)
        elif selected_type == "vitesse":
            result = conversion_vit(input, conv_type_in, conv_type_out)
        elif selected_type == "volume":
            result = conversion_vol(input, conv_type_in, conv_type_out)

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
            result = {f"Valeur ?? la position {params[0]}": fibonacci(params[0])}
        elif operator == "bernouilli":
            assert len(params) == 2 and params[0] > 0 and params[1] > 0
            experience = exp(params[0])
            bernouilli_array = bern(params[1], params[0])
            result = {"Nombre de face": f"{experience} sur {params[0]} lancers de pi??ces.", f"Nombre de face ?? chaque exp??rience de {params[0]} lancers de pi??ces": ', '.join(str(e) for e in bernouilli_array)}
        elif operator == "pythagore":
            assert len(params) == 2 and params[0] > 0 and params[1] > 0
            result = {"3??me c??t??": pythagore(params[0], params[1])}

    return render_template("calculation.html", data={
        'operators': [{
            'operator': 'fibonacci',
            'params': ['Position recherch??e']
        },
        {
            'operator': 'bernouilli',
            'params': ['Nombre de lancers de pi??ces', 'Nombre de fois o?? on r??p??te l\'exp??rience']
        },
        {
            'operator': 'pythagore',
            'params': ['1er c??t??', '2nd c??t??']
        }],
        "result": result,
    })


if __name__ == "__main__":
    app.run(debug=True)
