from sympy import Eq, solve, sympify
from sympy.parsing.sympy_parser import parse_expr


def solve_one_variable_equation(eq, result):
    assert isinstance(eq, str)
    assert isinstance(result, int) or isinstance(result, float)

    sympy_parse_eq = parse_expr(eq, evaluate=False)
    sympified_eq = sympify(sympy_parse_eq, convert_xor=True, evaluate=False, strict=True)
    equation = Eq(sympified_eq, result)

    return solve(equation)

