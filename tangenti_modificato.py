import numpy as np
import math

def is_valid(df, x0):
    return abs(df(x0)) > np.spacing(1)

def find_x(x0, m, f, df):
    return x0 - m*(f(x0) / df(x0))

def exit_statement():
    print("Newton : derivata nulla in x0")
    exit(0)

def newton_modificato(f, df, x0, m, tolx, tolf, max_iterations):
    x_list = []
    if is_valid(df, x0):
        x = find_x(x0, m, f, df)
        x_list.append(x)
    else:
        exit_statement()
    i = 1
    while i < max_iterations and \
        abs(f(x)) >= tolf and \
            abs(f(x0)/df(x0)) >= tolx*abs(x):
            x0 = x
            if is_valid(df, x0):
                x = find_x(x0, m, f, df)
            else:
                exit_statement()
            i = i + 1
    if i == max_iterations:
        print("max iterations reached")
    return x, i, x_list