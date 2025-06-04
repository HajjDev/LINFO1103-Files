# Euler's algorithm to find the PGCD
def pgcd(p, q):
    if q == 0: return p
    return pgcd(q, p % q)