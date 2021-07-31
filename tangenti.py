import numpy as np

def tangenti(f,df, x0, tol_x,tol_f, max_iterations ): 
     list = []
     i = 0
     while True:
        if (abs(df(x0)) > np.spacing(1)): #se e' inferiore ad eps e' nulla e si ferma
              x = x0 - (f(x0) / df(x0))
              list.append(x)
              i = i + 1
              x0 = x
        else:
            print("Derivata nulla in x0")
            break
        if (i < max_iterations and \
            abs(f(x)) >= tol_f and \
                abs(f(x0) / df(x0)) >= tol_x*abs(x)) == False:
                break
     return x, i,list
