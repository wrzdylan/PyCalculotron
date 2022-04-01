from PyCalculotron.components.calculator.basic_methods import substract


def test_substract():
    assert isinstance(substract(5, 3.8), int) or isinstance(substract(-5, 7.98), float)
