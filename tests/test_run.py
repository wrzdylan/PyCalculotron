from PyCalculotron.run import home, calculation


def test_index():
    assert home() == "Hello world !"


def test_calculation():
    assert calculation("fibonacci", 9) == {"result": 34}
