import numpy as np
import math

def sign(x):
    return math.copysign(1, x)

def bisezione(f, a, b, tol):
    if sign(f(a)) == sign(f(b)):
        return "You can't use this method on this interval"
    max_iterations = math.ceil(math.log((b - a) / tol) / math.log(2))
    list = []
    i = 0
    eps = np.spacing(1)
    while i < max_iterations and \
        abs(b - a) >= tol + eps*min(abs(a), abs(b)):
        x = a + (b - a)*0.5
        list.append(x)
        if f(x) == 0:
            return x, i + 1, list
        if sign(f(a)) != sign(f(x)):
            b = f(x)
        if sign(f(x)) != sign(f(b)):
            a = f(x)
	i = i + 1
    return x, i, list


