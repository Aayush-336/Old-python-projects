def eqs(a1, b1, c1, a2, b2, c2):
    sol_a = ((c1 * b2) - (c2 * b1)) / ((a1 * b2) - (a2 * b1))
    sol_b = (c1 - a1 * sol_a) / b1
    return sol_a, sol_b