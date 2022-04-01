from PyCalculotron.components.conversion.conversion_digit import conversion_digit

def test_conversion_digit():
    assert conversion_digit(1, "o", "bit") == 8
    assert conversion_digit(1, "ko", "o") == 1024
    assert conversion_digit(1, "mo", "o") == 1_048_576
    assert conversion_digit(1, "go", "o") == 1_073_741_824
    assert conversion_digit(1, "to", "o") == 1_099_511_627_776
    assert conversion_digit(1, "to", "bit") == 8796093022208