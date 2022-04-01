def add(x, y):
    assert isinstance(x, int) or isinstance(x, float)
    assert isinstance(y, int) or isinstance(y, float)
    return x + y


def substract(x, y):
    assert isinstance(x, int) or isinstance(x, float)
    assert isinstance(y, int) or isinstance(y, float)
    return x - y


def multiply(x, y):
    assert isinstance(x, int) or isinstance(x, float)
    assert isinstance(y, int) or isinstance(y, float)
    return x * y


def divide(x, y):
    assert isinstance(x, int) or isinstance(x, float)
    assert isinstance(y, int) or isinstance(y, float)
    return x / y


def percent(x, y):
    assert isinstance(x, int) or isinstance(x, float)
    assert isinstance(y, int) or isinstance(y, float)
    return (x / y) * 100
