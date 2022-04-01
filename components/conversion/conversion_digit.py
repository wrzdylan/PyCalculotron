CONVERT = {
"bit": 0.125, "o": 1.0, "ko": 1024, "mo": 1_048_576, "go": 1_073_741_824, "to": 1_099_511_627_776
}
def conversion_digit(input, conv_type_in, conv_type_out):
    """conversion de mémoire : "bit, octet, kilo-octet, mega-octet, giga-octet, tera-octet, mebioctet"
    Args:
        input (float): user input
        conv_type_in (str): type of conversion on input
        conv_type_out (str): type of conversion on output
    """
    return input*CONVERT[conv_type_in]/CONVERT[conv_type_out]
