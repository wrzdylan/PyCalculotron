from PyCalculotron.run import index, calculation

def test_index():
    assert index() == "Hello world !"

def test_calculation():
    assert calculation("fibonacci", 9) == {"result":34}
