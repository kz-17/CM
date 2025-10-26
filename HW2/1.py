import cmath
import sympy as sp
def root2(a, b, c):
    r1 = (-b+cmath.sqrt(b**2-4*a*c)) / 2*a
    r2 = (-b-cmath.sqrt(b**2-4*a*c)) / 2*a
    return r1, r2

x = sp.Symbol('x')
eq1 = x**2+x+1
x1, x2 = root2(1, 1, 1)
print('eq1 root:', root2(1, 1, 1))
print(cmath.isclose(x1, x2, rel_tol=1e-09, abs_tol=0.0))
print(x1**2+x1+1, x2**2+x2+1)

eq2 = x**2+2*x+1
x1, x2 = root2(1, 2, 1)
print('\neq2 root:', root2(1, 2, 1))
print(cmath.isclose(x1, x2, rel_tol=1e-09, abs_tol=0.0))
print(x1**2+2*x1+1, x2**2+2*x2+1)

eq2 = x**2-2*x-3
x1, x2 = root2(1, -2, -3)
print('\neq2 root:', root2(1, -2, -3))
print(cmath.isclose(x1, x2, rel_tol=1e-09, abs_tol=0.0))
print(x1**2-2*x1-3, x2**2-2*x2-3)
