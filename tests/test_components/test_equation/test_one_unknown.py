from PyCalculotron.components.equation.one_unknown import solve_one_variable_equation as sove


def test_sove():
    assert isinstance(sove(eq='3*x**2-(1/2)*x+(1/3)', result=4), int) or \
           isinstance(sove(eq='3*x**2-(1/2)*x+(1/3)', result=4), float) or \
           isinstance(sove(eq='3*x**2-(1/2)*x+(1/3)', result=4), list)

