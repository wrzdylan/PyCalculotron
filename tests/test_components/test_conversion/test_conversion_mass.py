from PyCalculotron.components.conversion.conversion_mass import conversion_mass

def test_conversion_mass():
    assert conversion_mass(1, "kg", "kg") == 1
    assert conversion_mass(1, "kg", "g") == 1000
    assert conversion_mass(1, "kg", "t") == 0.001

    assert conversion_mass(1, "g", "kg") == 0.001
    assert conversion_mass(1, "g", "g") == 1
    assert conversion_mass(1, "g", "t") == 0.000001

    assert conversion_mass(1, "t", "kg") == 1000
    assert conversion_mass(1, "t", "g") == 1000000
    assert conversion_mass(1, "t", "t") == 1

    assert conversion_mass(1, "mg", "kg") == 1e-6
    assert conversion_mass(1, "mg", "g") == 0.001

    assert conversion_mass(1, "lb", "kg") == 0.453592
    assert conversion_mass(1, "lb", "t") == 0.000453592
    assert conversion_mass(1, "lb", "g") == 453.592

    assert conversion_mass(1, "oz", "kg") == 0.028349499991789
    assert conversion_mass(1, "oz", "g") == 28.349499991788999154
    assert conversion_mass(1, "oz", "t") == 2.834949999178899835e-5