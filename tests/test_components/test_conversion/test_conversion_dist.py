from PyCalculotron.components.conversion.conversion_dist import conversion_dist

def test_conversion_dist():
    assert conversion_dist(20, "metre", "metre") == 20
    assert conversion_dist(20, "metre", "mile") == 0.01
    assert conversion_dist(20, "metre", "yard") == 21.88
    assert conversion_dist(20, "metre", "pied") == 65.62
    assert conversion_dist(20, "metre", "pouce") == 787.40
