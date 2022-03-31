from PyCalculotron.components.conversion.conversion_vit import conversion_vit

def test_conversion_vit():
    assert conversion_vit(20, "kmh", "kmh") == 20
    assert conversion_vit(20, "kmh", "mps") == 5.56
    assert conversion_vit(20, "kmh", "mph") == 12.43
    assert conversion_vit(20, "kmh", "noeud") == 10.8

