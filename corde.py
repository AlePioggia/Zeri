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