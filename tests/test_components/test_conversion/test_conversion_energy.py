from PyCalculotron.components.conversion.conversion_energy import conversion_energy

def test_conversion_energy():
    assert conversion_energy(1, "kJ", "W*h") == 0.2777777777777778
    assert conversion_energy(1, "kJ", "kW*h") == 0.0002777777777777778
    assert conversion_energy(1, "W*h", "kW*h") == 0.001
    assert conversion_energy(1, "kW*h", "cal") == 860400.0000000086 