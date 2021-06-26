def corde(f,df, x0, tol_x,tol_f, max_iterations ): #df() = f'()
     x = []
     m = df(x0)
     n_iterations = 0
     while True:
        x1 = x0 - (f(x0) / m) # Ricavata 
        n_iterations = n_iterations + 1
        x.append(x1)
        x0 = x1
        if (n_iterations < max_iterations and abs(f(x1) >= tol_f and abs(f(x0 / m)) >= tol_x * abs(x1))) == False:
            break
     return x1, n_iterations, x