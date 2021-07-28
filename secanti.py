#Doppio valore innesco
def secanti(f,x_minus_1, x0, tol_x,tol_f, max_iterations ): #x_minus_1 and x0 = valori d'innesco
     list = []
     i = 0
     while True:
        d = f(x0) * (x0 - x_minus_1) / (f(x0) - f(x_minus_1))
        x1 = x0 - d
        list.append(x1)  
        x_minus_1 = x0
        x0 = x1
        i = i + 1
        if (i < max_iterations and \
            abs(f(x1))>=tol_f and \
                abs(d)>=(tol_x * abs(x1))) == False:
                break
     return x1, i, list