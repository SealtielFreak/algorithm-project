from colorama import init, Fore, Style
from sympy.printing import pretty
from tabulate import tabulate

from lib.utility.utilities_pritting import fixing_float

init()


class pritting:
    @staticmethod
    def header(str, **kwargs):
        print(Style.BRIGHT)
        print(str, **kwargs)
        print(Style.RESET_ALL)

    @staticmethod
    def equation(equation, **kwargs):
        str_equation = pretty(equation, **kwargs)

        pritting.header("Ecuacion:")
        print(Fore.GREEN)
        print(str_equation)
        print(Style.RESET_ALL)

    @staticmethod
    def converge(converge, **kwargs):
        if len(converge) < 2:
            converge = converge[0]

        pritting.header("Convergencia:")
        print(Fore.GREEN)
        print(converge)
        print(Style.RESET_ALL)

    @staticmethod
    def tabulation(header, table, fix=3, **kwargs):
        fmt = fixing_float(len(header), fix)
        tabulation = tabulate(table, headers=header, floatfmt=fmt, **kwargs)

        pritting.header("Tabulacion:")
        print(Fore.GREEN)
        print(tabulation)
        print(Style.RESET_ALL)
