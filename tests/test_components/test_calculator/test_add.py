from PyCalculotron.components.calculator.basic_methods import add


def test_add():
    assert isinstance(add(5, 3.8), int) or isinstance(add(-5, 7.98), float)
