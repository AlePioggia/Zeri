import numpy as np
import math

def sign(x):
    return math.copysign(1, x)

def regula_falsi(f, a, b, tol, max_iterations):
    if sign(f(a)) == sign(f(b)):
        return [], 0, []
    x_list = []
    i = 0
    eps = np.spacing(1)
    x = a
    while i < max_iterations and \
        abs(f(x)) >= tol and \
            abs(b - a) >= tol + eps*max(abs(a), abs(b)):
            x = a -f(a)*(b-a)/(f(b)-f(a))
            x_list.append(x)
            i = i + 1
            if f(x) == 0:
                break
            if sign(f(a)) != sign(f(x)):
                b = x
            if sign(f(x)) != sign(f(b)):
                a = x
    return x, i, x_list


