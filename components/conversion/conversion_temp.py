def conversion_temp(temp, conv_type_in, conv_type_out):
    """conversion de temperatures : "celsius", "fahrenheit", "kelvin".
    Args:
        temp (float): user input
        conv_type_in (str): type of conversion on input
        conv_type_out (str): type of conversion on output
    """

    if conv_type_in == conv_type_out:
        return temp

    if conv_type_in == "celsius":
        if conv_type_out == "fahrenheit":
            return (temp * 9/5) + 32
        elif conv_type_out == "kelvin":
            return temp + 273.15

    if conv_type_in == "fahrenheit":
        if conv_type_out == "celsius":
            return round((temp - 32) * 5/9, 2)
        elif conv_type_out == "kelvin":
            return round((temp - 32) * 5/9 + 273.15, 2)

    if conv_type_in == "kelvin":
        if conv_type_out == "celsius":
            return round(temp - 273.15, 2)
        if conv_type_out == "fahrenheit":
            return round((temp - 273.15) * 9/5 + 32, 2)

