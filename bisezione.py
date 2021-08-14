import numpy as np
import math

def sign(x): return math.copysign(1, x)

def bisez(f, a, b, tol):
    if sign(f(a)) == sign(f(b)):
        print("You can't use this method on this interval")
        return [], 0, []
    max_iterations = int(math.ceil(math.log((b - a) / tol) / math.log(2)))
    x_list = []
    i = 0
    eps = np.spacing(1)
    while i < max_iterations and \
        abs(b - a) >= tol + eps*max(abs(a), abs(b)):
        x = a + (b - a)*0.5
        x_list.append(x)
        i = i + 1
        if f(x) == 0:
            break
        if sign(f(a)) != sign(f(x)):
            b = x
        if sign(f(x)) != sign(f(b)):
            a = x
    return x, i, x_list

