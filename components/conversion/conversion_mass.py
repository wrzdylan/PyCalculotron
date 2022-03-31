CONVERT = {"oz": 0.028349499991789, "mg":0.000001 , "g": 0.001, "kg": 1.0, "lb": 0.453592, "t": 1000.0}

def conversion_mass(mass, conv_type_in, conv_type_out):
    """conversion de masses : "Miligramme, Gramme, Kilogramme, Tonne, Pound, Ounce"
    Args:
        mass (float): user input
        conv_type_in (str): type of conversion on input
        conv_type_out (str): type of conversion on output
    """

    return mass*CONVERT[conv_type_in]/CONVERT[conv_type_out]

    