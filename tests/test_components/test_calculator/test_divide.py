from PyCalculotron.components.calculator.basic_methods import divide

def test_divide():
    assert isinstance(divide(5, 3.8), int) or isinstance(divide(-5, 7.98), float)
