import math

def pythagore(a, b):
    """Calculate hypotenuse

    Args:
        a (int): side A
        b (int): side B

    Returns:
        float: return hypotenuse from side A and side B
    """
    side_a = a
    side_b = b
    result = round(math.sqrt(side_a ** 2 + side_b ** 2), 4)
    return result