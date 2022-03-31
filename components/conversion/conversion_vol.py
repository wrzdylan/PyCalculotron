def conversion_vol(vol, conv_type_in, conv_type_out):
    """conversion de volume : "Litre", "Baril de pétrole", "Mètre cube", "Centimètre cube", "Gallon (US)".

    Args:
        vol (float): user input
        conv_type_in (str): type of conversion on input
        conv_type_out (str): type of conversion on output
    """

    if conv_type_in == conv_type_out:
        return vol

    if conv_type_in == "litre":
        if conv_type_out == "baril":
            return round(vol / 159, 2)
        if conv_type_out == "m_cube":
            return round(vol / 1000, 2)
        if conv_type_out == "cm_cube":
            return round(vol * 1000, 2)
        if conv_type_out == "gallon":
            return round(vol / 3.785, 2)

    if conv_type_in == "baril":
        if conv_type_out == "litre":
            return round(vol * 159, 2)
        if conv_type_out == "m_cube":
            return round(vol / 6.29, 2)
        if conv_type_out == "cm_cube":
            return round(vol * 158987, 2)
        if conv_type_out == "gallon":
            return round(vol * 42, 2)

    if conv_type_in == "m_cube":
        if conv_type_out == "baril":
            return round(vol * 6.29, 2)
        if conv_type_out == "litre":
            return round(vol * 1000, 2)
        if conv_type_out == "cm_cube":
            return round(vol * (1+0.00001)+6, 2)
        if conv_type_out == "gallon":
            return round(vol * 264, 2)

    if conv_type_in == "cm_cube":
        if conv_type_out == "baril":
            return round(vol / 158987, 2)
        if conv_type_out == "m_cube":
            return round(vol / (1+0.00001)+6, 2)
        if conv_type_out == "litre":
            return round(vol / 1000, 2)
        if conv_type_out == "gallon":
            return round(vol / 3785, 2)

    if conv_type_in == "gallon":
        if conv_type_out == "baril":
            return round(vol / 42, 2)
        if conv_type_out == "m_cube":
            return round(vol / 264, 2)
        if conv_type_out == "cm_cube":
            return round(vol * 3785, 2)
        if conv_type_out == "litre":
            return round(vol * 3.785, 2)
            