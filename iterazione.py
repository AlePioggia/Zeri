import math

def iterazione(g, x0, tolx, max_iterations):
    x_list = []
    i = 0
    while True:
        x = g(x0)
        list.append(x)
        d = x - x0
        x0 = x
        i = i + 1
        if i < max_iterations and \
            abs(d) >= tolx*abs(x):
            break
    return x, i, x_list        