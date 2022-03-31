from PyCalculotron.components.conversion.conversion_digit import conversion_digit

def test_conversion_digit():
    assert conversion_digit(1, "o", "bit") == 8
    assert conversion_digit(1, "o", "ko") == 1024
    assert conversion_digit(1, "o", "mo") == 1_048_576
    assert conversion_digit(1, "o", "go") == 1_073_741_824
    assert conversion_digit(1, "o", "to") == 1_099_511_627_776