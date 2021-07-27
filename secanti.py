#Doppio valore innesco
def secanti(f,x_minus_1, x0, tol_x,tol_f, max_iterations ): #x_minus_1 and x0 = valori d'innesco
     list = []
     i = 0
     while True:
        m = (f(x0) - f(x_minus_1)) / (x0 - x_minus_1) #coefficiente angolare secante
        x1 = x0 - (f(x0) / m) # x0 - distanza fra x0 e x1 = x1
        list.append(x1)  
        x_minus_1 = x0
        x0 = x1
        i = i + 1
        if ( i < max_iterations and \
            abs(f(x1))>=tol_x and \
                abs(f(x0)/m)>=(tol_x * abs(x1)) == False ):
                break
     return x1, i, list