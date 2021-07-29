import numpy as np
import math

def sign(x):
    return math.copysign(1, x)

def regula_falsi(f, a, b, tol, max_iterations):
    if sign(f(a)) == sign(f(b)):
        return 0, 0, []
    x_list = []
    i = 0
    eps = np.spacing(1)
    x = f(a)
    while i < max_iterations and \
        abs(f(x)) >= tol and \
            abs(b - a) >= tol + eps*max(abs(a), abs(b)):
            x = -f(a)*((b - a)/f(b) - f(a)) + a
            x_list.append(x)
            if f(x) == 0:
                return 0, 0, []
            if sign(f(a)) != sign(f(x)):
                b = f(x)
            if sign(f(x)) != sign(f(x)):
                a = f(x)
            i = i + 1


