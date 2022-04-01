from PyCalculotron.components.calculator.basic_methods import multiply


def test_multiply():
    assert isinstance(multiply(5, 3.8), int) or isinstance(multiply(-5, 7.98), float)
