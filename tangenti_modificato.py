import numpy as np
import math

def tangenti_modificato(f,df, x0, tolx, tolf, m, max_iterations): 
    x_list = []
    eps = np.spacing(1)
    i = 0
    while True:
        if (abs(df(x0)) > eps): #se e' inferiore ad eps e' nulla e si ferma
            x = x0 - m*(f(x0)/df(x0))
            x_list.append(x)
            i = i + 1
            x0 = x
        else:
            print("Derivata nulla in x0")
            break
        if (i < max_iterations and \
            abs(f(x)) >= tolf and \
                abs(f(x0) / df(x0)) >= tolx*abs(x)) == False:
                break
    return x, i,x_list