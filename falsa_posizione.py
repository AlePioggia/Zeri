import numpy as np
import math

def sign(x) : return math.copysign(1, x) #Ritorna 1 se x > 0, -1 se x < 0, 0 se b è 0

def check_tolerance(a, b, eps, tol):
    return abs(b - a) >= tol + eps * max(abs(a), abs(b))

def regula_falsi(f, a, b, tol, max_iterations):
    eps = 2**52
    if sign(f(a) == sign(f(b))) > 0:
        exit()
    n_iterations = 0
    x = []
    while n_iterations < max_iterations and check_tolerance(a, b, eps, tol) and abs(f(a)) >= tol:
        alpha = a - f(a) * (b - a) / (f(b) - f(a))
        x.append(alpha)
        n_iterations = n_iterations + 1
        if f(alpha) == 0:
            break
        elif sign(f(alpha) == sign(f(a))) > 0:
            a = alpha 
        elif sign(f(alpha)) == sign(f(b)) < 0:
            b = alpha
    return alpha, n_iterations, x
        


