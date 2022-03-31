def conversion_dist(dist, conv_type_in, conv_type_out):
    """conversion de distance : "mètre", "Mile", "Pouce", "Pied", "Yard".

    Args:
        dist (float): user input
        conv_type_in (str): type of conversion on input
        conv_type_out (str): type of conversion on output
    """

    if conv_type_in == conv_type_out:
        return dist

    if conv_type_in == "metre":
        if conv_type_out == "mile":
            return round(dist / 1609, 2)
        if conv_type_out == "pouce":
            return round(dist * 39.37, 2)
        if conv_type_out == "pied":
            return round(dist * 3.281, 2)
        if conv_type_out == "yard":
            return round(dist * 1.094, 2)

    if conv_type_in == "mile":
        if conv_type_out == "metre":
            return round(dist * 1609, 2)
        if conv_type_out == "pouce":
            return round(dist * 63360, 2)
        if conv_type_out == "pied":
            return round(dist * 5280, 2)
        if conv_type_out == "yard":
            return round(dist * 1760, 2)

    if conv_type_in == "pouce":
        if conv_type_out == "metre":
            return round(dist / 39.37, 2)
        if conv_type_out == "mile":
            return round(dist / 63360, 2)
        if conv_type_out == "pied":
            return round(dist / 12, 2)
        if conv_type_out == "yard":
            return round(dist / 36, 2)

    if conv_type_in == "pied":
        if conv_type_out == "metre":
            return round(dist / 3.281, 2)
        if conv_type_out == "mile":
            return round(dist / 5280, 2)
        if conv_type_out == "pouce":
            return round(dist * 12, 2)
        if conv_type_out == "yard":
            return round(dist / 3, 2)

    if conv_type_in == "yard":
        if conv_type_out == "metre":
            return round(dist / 1.094, 2)
        if conv_type_out == "mile":
            return round(dist / 1760, 2)
        if conv_type_out == "pouce":
            return round(dist * 36, 2)
        if conv_type_out == "pied":
            return round(dist * 3, 2)