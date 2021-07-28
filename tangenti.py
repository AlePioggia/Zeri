import numpy as np

#per df si intende la derivata
#Versione personale attualmente sbagliata 
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

#versione della prof
def newton(f,df, x0, tol_x,tol_f, max_iterations ):
    list = []
    eps = np.spacing(1)
    i = 1
    if abs(df(x0)) > eps:
        x = x0 - f(x0)/df(x0)
        list.append(x)
    else:
        print("Newton : Derivata nulla in x0")
        return [], 0, []
    while i < max_iterations and \
        abs(f(x)) >= tol_f and \
            abs(f(x0)/ df(x0)) >= tol_x*abs(x):
            x0 = x
            if abs(df(x0)) > eps:
                x = x0 - f(x0)/df(x0)
                list.append(x)
                i = i + 1
            else:
                print("Newton : Derivata nulla in x0")
                return [], 0, []
            if i == max_iterations:
                print("Newton : Raggiunto il massimo numero di iterazioni")
    return x, i, list