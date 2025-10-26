
import sympy as sp

def f(x):
    return x**3

def df(expr, var):
    return sp.diff(expr, var)

def integratal(expr, x, a, b):
    return sp.integrate(expr, (x, a, b))

if __name__ == '__main__':
    x = sp.Symbol('x')
    print('diff:', df(f(x), x))
    print('integratal: ', integratal(f(x), x, 0, 3))
