from PyCalculotron.components.conversion.conversion_temp import conversion_temp

def test_conversion_temp():
    assert conversion_temp(20, "celsius", "celsius") == 20
    assert conversion_temp(20, "celsius", "fahrenheit") == 68
    assert conversion_temp(20, "celsius", "kelvin") == 293.15
    assert conversion_temp(20, "fahrenheit", "celsius") == -6.67
    assert conversion_temp(20, "fahrenheit", "kelvin") == 266.48
    assert conversion_temp(20, "kelvin", "celsius") == -253.15
    assert conversion_temp(20, "kelvin", "fahrenheit") == -423.67