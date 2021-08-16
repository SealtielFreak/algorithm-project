from sympy import symbols
from sympy.core.numbers import NaN, Infinity
from lib.exception.exception_argument import ExpressionNoComputable


def positive(value):
    try:
        protect(value)
    except ExpressionNoComputable:
        return value
        
    if value <= 0:
        value *= -1

    return value


def protect(*args):
    for arg in args:
        if type(arg) in [list, dict]:
            raise TypeError
    
        if type(arg) in [NaN, Infinity]:
            raise ExpressionNoComputable


class utilities:
    @staticmethod
    def error_a(exact, aproximate):
        return abs(exact - aproximate)

    @staticmethod
    def error_r(exact, aproximate):
        try:
            error = utilities.error_a(exact, aproximate) / exact
            return positive(error)
        except ZeroDivisionError:
            return 1

    @staticmethod
    def tabulation(r_it):
        if type(r_it) is list:
            for it in list(r_it):
                yield it
        else:
            for it in range(1, r_it + 1):
                yield it

    @staticmethod
    def arg_symbol(args_symbol):
        symbol = symbols("x")

        if "symbol" in args_symbol:
            symbol = args_symbol["symbol"]

        return symbol
