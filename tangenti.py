import numpy as np

#per df si intende la derivata
def tangenti(f,df, x0, tol_x,tol_f, max_iterations ): #x_minus_1 and x0 = valori d'innesco
     list = []
     m = df(x0)
     i = 0
     while True:
        if (abs(df(x0)) > np.spacing(1)): #se e' inferiore ad eps e' nulla e si ferma
              x = x0 - (f(x0) / m)
              list.append(x)
              i = i + 1
        else:
            print("Derivata nulla in x0")
            break
        if (i < max_iterations and \
            abs(f(x)) >= tol_f and \
                abs(f(x0) / m) >= tol_x*abs(x)) == False:
                break
     return x, i,list