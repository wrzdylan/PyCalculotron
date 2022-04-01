from PyCalculotron.components.calculator.basic_methods import percent


def test_percent():
    assert isinstance(percent(5, 3.8), int) or isinstance(percent(-5, 7.98), float)
