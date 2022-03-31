from PyCalculotron.components.conversion.conversion_vol import conversion_vol

def test_conversion_vol():
    assert conversion_vol(20, "litre", "litre") == 20
    assert conversion_vol(20, "litre", "baril") == 0.13
    assert conversion_vol(20, "litre", "m_cube") == 0.02
    assert conversion_vol(20, "litre", "cm_cube") == 20000
    assert conversion_vol(20, "litre", "gallon") == 5.28
    