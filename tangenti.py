import numpy as np

#per df si intende la derivata
def tangenti(f,df, x0, tol_x,tol_f, max_iterations ): #x_minus_1 and x0 = valori d'innesco
     x = []
     n_iterations = 0
     while True:
        if (abs(df(x0)) > np.spacing(1)): #se e' inferiore ad eps e' nulla e si ferma
              x1 = x0 - (f(x0) / df(x0))
              x.append(x1)
              n_iterations = n_iterations + 1
        else:
            print("Derivata nulla in x0")
            break
        if ((n_iterations < max_iterations) and
            (abs(f(x1)) >= tol_f and abs(f(x0) / df(x0) >= tol_x*abs(x1)))) == False:
            break
     return x1, n_iterations,x