def eh_par(n):
    """True se n for par, False se for ímpar."""
    return n % 2 == 0     # a comparação já é True ou False: não precisa de if

print(eh_par(10))   # True
print(eh_par(10))    # False