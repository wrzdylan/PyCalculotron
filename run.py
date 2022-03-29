from flask import Flask, render_template
from PyCalculotron.components.calculation.fibonacci import fibonacci

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/calculation/<operation>/<params>')
def calculation(operation, params):
    if operation == "fibonacci":
        assert params > 0
        result = fibonacci(params)

    return render_template("calculation.html", data={
        "result":result
    })

if __name__ == "__main__":
    app.run(debug=True)