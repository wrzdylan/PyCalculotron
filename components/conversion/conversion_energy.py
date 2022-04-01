CONVERT = {
"J": 0.001, "kJ": 1.0, "cal": 0.00418410041841, "kcal": 4.184, "W*h": 3.6, "kW*h": 3600
}
def conversion_energy(input, conv_type_in, conv_type_out):
    """conversion de mémoire : "joule, kilojoule, calorie, kilocalorie, watt-heure, kilowatt-heure"
    Args:
        input (float): user input
        conv_type_in (str): type of conversion on input
        conv_type_out (str): type of conversion on output
    """
    return input*CONVERT[conv_type_in]/CONVERT[conv_type_out]
