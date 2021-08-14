import math

def iterazione(g, x0, tolx, max_iterations):
    x_list = []
    i = 0
    while True:
        x_list.append(x0) if i == 0 else print("it", i)
        x = g(x0)
        x_list.append(x)
        d = x - x0
        i = i + 1
        x0 = x
        if not (i <= max_iterations and \
            abs(d) >= tolx*abs(x)):
            break
    return x, i, x_list        