
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

def regula_falsi(f, a, b, tol, max_iterations):
    if sign(f(a)) == sign(f(b)):
        return [], 0, []
    x_list = []
    i = 0
    eps = np.spacing(1)
    x = a
    while i < max_iterations and \
        abs(f(x)) >= tol and \
            abs(b - a) >= tol + eps*max(abs(a), abs(b)):
            x = a -f(a)*(b-a)/(f(b)-f(a))
            x_list.append(x)
            i = i + 1
            if f(x) == 0:
                break
            if sign(f(a)) != sign(f(x)):
                b = x
            if sign(f(x)) != sign(f(b)):
                a = x
    return x, i, x_list

def corde(f,df, x0, tol_x,tol_f, max_iterations ): #df() = f'()
    list = []
    m = df(x0)
    i = 0
    while True:
        x = x0 - (f(x0) / m)
        i = i + 1
        list.append(x)
        x0 = x
        if (i < max_iterations and \
            abs(f(x) >= tol_f and \
                abs(f(x0) / m) >= tol_x * abs(x))) == False:
                break
    return x, i, list

def secanti(f,x_minus_1, x0, tol_x,tol_f, max_iterations ): #x_minus_1 and x0 = valori d'innesco
    list = []
    i = 0
    while True:
        d = f(x0)*((x0 - x_minus_1)/(f(x0)-f(x_minus_1)))
        x1 = x0 - d
        list.append(x1)  
        x_minus_1 = x0
        x0 = x1
        i = i + 1
        if ( i < max_iterations and \
            abs(f(x1))>=tol_f and \
                abs(d)>=(tol_x * abs(x1))) == False :
                break
    return x1, i, list

def newton(f,df, x0, tol_x,tol_f, max_iterations ): #x_minus_1 and x0 = valori d'innesco
    list = []
    m = df(x0)
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

def set_numerator(x_list, i, k):
    return np.log(abs(x_list[k + 2] - x_list[k + 3]) / abs(x_list[k + 1] - x_list[k + 2]))
def set_denominator(x_list, i, k):
    return np.log(abs(x_list[k + 1] - x_list[k + 2]) / abs(x_list[k] - x_list[k + 1]))
def stima_ordine(x_list,i):
    p=[]
    for k in range(i-3):
        p = []
        numerator = set_numerator(x_list, i, k)
        denominator = set_denominator(x_list, i, k)
        p.append(numerator/denominator)
        ordine=p[-1]
    return ordine

def newton_m(f,df, x0, tolx, tolf, m, max_iterations): 
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