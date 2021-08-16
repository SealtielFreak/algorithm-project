#!/usr/bin/python

# MIT License
#
# Copyright (c) 2021 Jesus Adrian Flores, Diego Sealtiel Valderrama García
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from lib.algorithms.functions import bisection, secant, fixed_point, newton_raphson, regular_falsi
from lib.exception.exception_argument import InvalidConverge, InvalidExpression, ExpressionNoComputable, MethodNotAppropriate
from lib.ArgumentParser import ArgumentParser
from lib.priting import pritting
from sympy.parsing.sympy_parser import parse_expr

intro = """

         __                 _ __                
  ____ _/ /___ _____  _____(_) /_____ ___  ____ 
 / __ `/ / __ `/ __ \/ ___/ / __/ __ `__ \/ __ \\
/ /_/ / / /_/ / /_/ / /  / / /_/ / / / / / /_/ /
\__,_/_/\__, /\____/_/  /_/\__/_/ /_/ /_/\____/ 
       /____/                                   


"""

dictionary = {
    "biseccion": bisection,
    "secante": secant,
    "regla-falsa": regular_falsi,
    "punto-fijo": fixed_point,
    "newton-raphson": newton_raphson,
}

sys_argument = ArgumentParser(
    prog="Algoritmo"
)

sys_argument.add_argument(
    "method",
    type=str,
    choices=dictionary.keys(),
    help="Seleccione el metodo numerico"
)

sys_argument.add_argument(
    "equation",
    type=str,
    nargs='+',
    help="Entrada de la expresion algebraica a resolver"
)

sys_argument.add_argument(
    "--n_it", "-n",
    type=int,
    action="store",
    required=True,
    help="Numero de iteraciones"
)

sys_argument.add_argument(
    "--converge", "-c",
    type=float,
    nargs='+',
    action="store",
    required=True,
    help="Rango de iteracion de la convergencia"
)

sys_argument.add_argument(
    "--symbol", "-s",
    type=str,
    default="x",
    action="store",
    required=False,
    help="Ingrese la incognita a despejar"
)

sys_argument.add_argument(
    "--fix", "-f",
    type=int,
    default=4,
    action="store",
    required=False,
    help="numero de cifras significativas"
)

sys_argument.add_argument(
    "--version", "-v",
    action="version",
    help="Ver informacion acerca del programa",
    version="Algoritmo <0.0.b5>"
)

if __name__ == "__main__":
    status = 1

    args = sys_argument.parse_args()

    method = args.method
    symbol = args.symbol
    equation = "".join(args.equation)
    converge = args.converge
    n_it = args.n_it
    fix = args.fix

    try:
        header, table = [], []

        try:
            symbol = parse_expr(symbol)
            equation = parse_expr(equation)
        except TypeError:
            raise InvalidExpression

        if method in ["biseccion", "secante", "regla-falsa"] and len(converge) == 2:
            if converge[0] >= converge[1]:
                raise InvalidConverge
            header, table = dictionary[method](equation, converge, n_it)
        elif method in ["newton-raphson", "punto-fijo"] and len(converge) == 1:
            header, table = dictionary[method](equation, converge[0], n_it)
        else:
            raise InvalidConverge

        pritting.equation(equation, use_unicode=False)
        pritting.converge(converge)
        pritting.tabulation(header, table, fix, tablefmt="simple")
        status = 0

    except InvalidExpression:
        sys_argument.error("Expresion de ecuacion invalida")
    except InvalidConverge:
        sys_argument.error("Numero invalido de convergencia, intente con otro")
    except ExpressionNoComputable:
        sys_argument.error("Datos no computeables, revise y cambie sus entradas")
    except MethodNotAppropriate:
        sys_argument.error("Metodo no apropiado, intente con otro metodo numerico")
    except KeyboardInterrupt:
        pass

    if status != 0:
        print(args)

    exit(status)
