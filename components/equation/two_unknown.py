from sympy import symbols, Eq, solve, sympify
from sympy.parsing.sympy_parser import parse_expr


def solve_two_variable_equation(eq1, eq2, res_1, res_2):
    assert isinstance(eq1, str) and isinstance(eq2, str)

    x, y = symbols('x, y')

    sympy_parse_eq1 = parse_expr(eq1, evaluate=False)
    sympy_parse_eq2 = parse_expr(eq2, evaluate=False)

    sympified_eq1 = sympify(sympy_parse_eq1, convert_xor=True, evaluate=False, strict=True)
    sympified_eq2 = sympify(sympy_parse_eq2, convert_xor=True, evaluate=False, strict=True)

    equality_1 = Eq(sympified_eq1, res_1)
    equality_2 = Eq(sympified_eq2, res_2)

    return solve((equality_1, equality_2), (x, y))


solve_two_variable_equation(eq1='3*x**2-5*y+2', eq2='2*x+y-1/2', res_1=8, res_2=3)
