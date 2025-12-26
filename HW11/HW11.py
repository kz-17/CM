import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    """
    Solve a homogeneous linear ODE with constant coefficients.

    Parameters
    ----------
    coefficients : list
        [a_n, a_{n-1}, ..., a_0] for the ODE:
        a_n y^(n) + ... + a_0 y = 0

    Returns
    -------
    solution_terms : list of strings
        Basis functions of the general solution.
    """

    # Step 1: solve characteristic equation
    roots = np.roots(coefficients)

    # Step 2: group roots (handle multiplicity)
    rounded_roots = [complex(round(r.real, 6), round(r.imag, 6)) for r in roots]
    root_counts = Counter(rounded_roots)

    solution_terms = []

    # Step 3: build general solution
    for r, multiplicity in root_counts.items():
        if abs(r.imag) < 1e-6:  # real root
            for k in range(multiplicity):
                if k == 0:
                    solution_terms.append(f"e^({r.real} x)")
                else:
                    solution_terms.append(f"x^{k} e^({r.real} x)")
        else:  # complex root
            alpha = r.real
            beta = abs(r.imag)
            solution_terms.append(f"e^({alpha} x) cos({beta} x)")
            solution_terms.append(f"e^({alpha} x) sin({beta} x)")

    return solution_terms
