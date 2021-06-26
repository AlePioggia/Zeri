import numpy as np
import math


def sign(x) : return math.copysign(1, x) #Ritorna 1 se x > 0, -1 se x < 0, 0 se b è 0

def check_tolerance(a, b, eps, tol):
    return abs(b - a) >= tol + eps * max(abs(a), abs(b))
def set_max_iterations(a, b, eps, tol):
    return int(math.ceil(math.log((b - a) / tol) / math.log(2)))

def bisez(f, a, b, tol):
    eps = 2**52
    if sign(f(a)) == sign(f(b)):
        exit()
    max_iterations = set_max_iterations(a, b, eps, tol)
    n_iterations = 0
    x = []
    while n_iterations < max_iterations and check_tolerance(a, b, eps, tol):
        alpha = (a + (b - a)) / 2
        x.append(alpha)
        n_iterations = n_iterations + 1
        if f(alpha) == 0:
            break
        elif sign(f(a)) == sign(f(alpha)) > 0:
            a = alpha
        elif sign(f(b)) == sign(f(alpha)) > 0:
            b = alpha
    return alpha, n_iterations, x
        


