from PyCalculotron.components.equation.two_unknown import solve_two_variable_equation as stve


def test_stve():
    assert isinstance(stve(eq1='3*x**2-5*y+2', eq2='2*x+y-1/2', res_1=8, res_2=3), list) or \
           isinstance(stve(eq1='3*x**2-5*y+2', eq2='2*x+y-1/2', res_1=8, res_2=3), tuple)
