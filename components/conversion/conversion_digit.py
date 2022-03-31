CONVERT = {
"bit": 0.125, "o": 1.0, "ko": 0.0009765625, "mo": 9.5367431640625e-7, "go": 9.313225746154785e-10, "to": 9.094947017729282e-13
}
def conversion_digit(input, conv_type_in, conv_type_out):
    """conversion de mémoire : "bit, octet, kilo-octet, mega-octet, giga-octet, tera-octet, mebioctet"
    Args:
        input (float): user input
        conv_type_in (str): type of conversion on input
        conv_type_out (str): type of conversion on output
    """
    return input*CONVERT[conv_type_in]/CONVERT[conv_type_out]
