from lib.utility.utilities_algorithm import utilities, protect
from lib.exception.exception_argument import MethodNotAppropriate, ExpressionNoComputable


def bisection(equation, r_it, n_it, **kwargs):
    table = []

    symbol = utilities.arg_symbol(kwargs)

    eq = equation
    a, b = r_it
    d = 0

    for it in utilities.tabulation(n_it):
        c = (a + b) / 2

        f_c = eq.subs(symbol, c)
        m = f_c * eq.subs(symbol, a)

        err_a = utilities.error_a(d, c)
        err_r = utilities.error_r(d, c)

        table.append([it, a, b, m, c, f_c, err_a, err_r])

        if m > 0:
            a = c
        else:
            b = c

        d = c

    return ("it", "a", "b", "m", "c", "f(c)", "Error A", "Error R"), table



def regular_falsi(equation, r_it, n_it, **kwargs):
    table = []
    
    symbol = utilities.arg_symbol(kwargs)
    
    x_a, x_b = r_it
    x_k = 0
    
    for it in utilities.tabulation(n_it):
        f_xa = equation.subs(symbol, x_a)
        f_xb = equation.subs(symbol, x_b)
        
        x_r = ((x_a * f_xb) - (x_b * f_xa)) / (f_xb - f_xa)
        f_xr = equation.subs(symbol, x_r)
        
        err_a = utilities.error_a(x_r, x_k)
        err_r = utilities.error_a(x_r, x_k)
        
        table.append([it, x_a, x_b, x_r, f_xr, err_a, err_r])
        
        try:
            protect(x_r)
        except ExpressionNoComputable:
            break
        
        if x_r > 0:
            x_a = x_r
        else:
            x_b = x_r

        x_k = x_r
    
    return ("it", "x_a", "x_b", "x_r", "f(x_r)", "Error A", "Error R"), table
    
    
def secant(equation, r_it, n_it, **kwargs):
    table = []
    
    symbol = utilities.arg_symbol(kwargs)

    eq = equation
    x_i, x_j = r_it

    for it in utilities.tabulation(n_it):
        xf_i = eq.subs(symbol, x_i)
        xf_j = eq.subs(symbol, x_j)

        x_k = x_j - ((xf_j * (x_i - x_j)) / (xf_i - xf_j))
        
        xf_k = eq.subs(symbol, x_k)
        
        err_a = utilities.error_a(x_k, x_j)
        err_r = utilities.error_r(x_k, x_j)

        table.append([it, x_i, x_j, x_k, xf_k, err_a, err_r])
        
        try:
            protect(x_i, x_j)
        except ExpressionNoComputable:
            break
        
        
        x_i, x_j = x_j, x_k

        it += 1

    return ("it", "x_i", "x_j", "x_k", "f(x_k)", "Error A", "Error R"), table


def fixed_point(equation, c_it, n_it, **kwargs):
    table = []

    symbol = utilities.arg_symbol(kwargs)

    eq_0 = equation
    eq_1 = equation + symbol
    x_0 = c_it
    
    if eq_1.subs(symbol, c_it) > eq_0.subs(symbol, c_it):
        raise MethodNotAppropriate
    
    for it in utilities.tabulation(n_it):
        x_1 = eq_1.subs(symbol, x_0)
        
        xf_1 = eq_0.subs(symbol, x_1)
        
        err_a = utilities.error_a(x_0, x_1)
        err_r = utilities.error_r(x_0, x_1)

        table.append([it, x_0, x_1, xf_1, err_a, err_r])

        x_0 = x_1

    return ("it", "x_0", "x_1", "f(x_1)", "Error A", "Error R"), table


def newton_raphson(equation, c_it, n_it, **kwargs):
    table = []

    symbol = utilities.arg_symbol(kwargs)

    eq_0 = equation
    x_0 = c_it

    eq_1 = eq_0.diff(symbol)

    for it in utilities.tabulation(n_it):
        x_i = eq_0.subs(symbol, x_0)
        x_j = eq_1.subs(symbol, x_0)
        x_k = x_0 - (x_i / x_j)
        
        xf_k = eq_0.subs(symbol, x_k)
        
        err_a = utilities.error_a(x_k, x_0)
        err_r = utilities.error_r(x_k, x_0)
        
        table.append([it, x_i, x_j, x_k, xf_k, err_a, err_r])
        
        x_0 = x_k

    return ("it", "x_i", "x_j", "x_k", "f(x_k)", "Error A", "Error R"), table


def lagrange(points, **kwargs): ...


def jacobi(**kwargs): ...


def jacobi_gaus_seidel(**kwargs): ...
