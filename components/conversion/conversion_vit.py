def conversion_vit(vit, conv_type_in, conv_type_out):
    """conversion de vitesse : "Kilometre par heure", "Metre par seconde", "Mille par heure", "Noeuds".
    Args:
        vit (float): user input
        conv_type_in (str): type of conversion on input
        conv_type_out (str): type of conversion on output
    """

    if conv_type_in == conv_type_out:
        return vit

    if conv_type_in == "kmh":
        if conv_type_out == "mps":
            return round(vit / 3.6, 2)
        if conv_type_out == "mph":
            return round(vit / 1.609, 2)
        if conv_type_out == "noeud":
            return round(vit / 1.852, 2)

    if conv_type_in == "mps":
        if conv_type_out == "kmh":
            return round(vit * 3.6, 2)
        if conv_type_out == "mph":
            return round(vit * 2.237, 2)
        if conv_type_out == "noeud":
            return round(vit * 1.944, 2)

    if conv_type_in == "mph":
        if conv_type_out == "mps":
            return round(vit / 2.237, 2)
        if conv_type_out == "kmh":
            return round(vit * 1.609, 2)
        if conv_type_out == "noeud":
            return round(vit / 1.151, 2)

    if conv_type_in == "noeud":
        if conv_type_out == "mps":
            return round(vit / 1.944, 2)
        if conv_type_out == "kmh":
            return round(vit * 1.852, 2)
        if conv_type_out == "mph":
            return round(vit / 1.151, 2)
