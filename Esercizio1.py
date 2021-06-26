import numpy as np 
import sympy as sym
import bisezione
import falsa_posizione
import secanti
import tangenti
import corde
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify

def stima_ordine(xk, num_iterations):
      p = []
      for k in range(num_iterations - 3):
         p.append( np.log( abs(xk[k+2] - xk[k+3]) / abs(xk[k+1] - xk[k+2]))/ np.log( abs(xk[k+1]-xk[k+2] ) / abs(xk[k]-xk[k+1])))
      ordine = p[-1]
      return ordine

def show_errors(x_list, x_num_iterations, f_names):
    if (len(x_list) != len(x_num_iterations) != len(f_names)):
        print("The lists should have the same size!")
    for i in range(0, len(x_list)):
        print("Funzione ", f_names[i], "Ordine di convergenza ",stima_ordine(x_list[i], x_num_iterations[i]))
        i = i + 1


def error_value(x, alpha):
    return np.abs(np.array(x - alpha))

def draw_chart(a, b, linspace_range, p_f):
    z = np.linspace(a, b, linspace_range)
    plt.plot(z, 0*z, z, p_f(z), 'r-')
    plt.show()

#6 arguments = (simbolic_function, zero value, interval_left_side, interval_right_side,
#               x0, x_minus_1), the 6th is needed only for the secants method
choice = input("Choose the function ") 
x = sym.symbols('x') #permette di poter utilizzare il simbolo anche se non definito
functions_menu = {
    '1' : [sym.exp(x)-(x+1), 0, -1, 2, -0.5, -0.3],
    '2' : [sym.log(x + 3, 2) - 2, 1, -1, 2, -0.5, 0.5], 
    '3' : [sym.sqrt(x) - x**2/4, 2**(4/3), 1, 3, 1.8, 1.5]  
}
picked_function = functions_menu.get(choice)
f, alpha, a, b, x0, x_minus_1 = picked_function #spacchetto
df = sym.diff(f, x, 1) #calcolo la derivata di f in x rispetto al primo grado
p_f = lambdify(x, f, np) #traslo la funzione in una python function passando da numpy
p_df = lambdify(x, df, np) #... faccio lo stesso con la sua derivata
draw_chart(a, b, 100, p_f) #disegna il grafico
tol_x = 1e-12
tol_f = 1e-12
max_iterations = 500
bis_alpha, bis_num_iterations, bis_x = bisezione.bisez(p_f, a, b, tol_x) #applico bisezione
falsi_alpha, falsi_num_iterations, falsi_x = falsa_posizione.regula_falsi(p_f, a, b, tol_x, max_iterations) #applico regula_falsi
corde_alpha, corde_num_iterations, corde_x = corde.corde(p_f, p_df, x0, tol_x, tol_f, max_iterations) #applico corde
sec_alpha, sec_num_iterations, sec_x = secanti.secanti(p_f, x_minus_1, x0, tol_x, tol_f, max_iterations) #applico secanti
newton_alpha, newton_num_iterations, newton_x = tangenti.tangenti(p_f, p_df, x0, tol_x, tol_f, max_iterations) #applico newton(aka tangenti)
plt.semilogy(
            range(bis_num_iterations), error_value(bis_x, alpha), 'go-',
            range(falsi_num_iterations), error_value(falsi_num_iterations, alpha), 'bo-',
            range(corde_num_iterations), error_value(corde_num_iterations, alpha), 'mo-',
            range(sec_num_iterations), error_value(sec_num_iterations, alpha), 'co-',
            range(newton_num_iterations), error_value(newton_num_iterations, alpha), 'ro-'          
            )
f_names = ['Bisezione', 'Regula False', 'Corde', 'Secanti', 'Newton']
plt.legend(f_names)
x_list = [bis_x, falsi_x, corde_x, sec_x, newton_x]
x_num_iterations = [bis_num_iterations, falsi_num_iterations, corde_num_iterations, sec_num_iterations, newton_num_iterations]
show_errors(x_list, x_num_iterations, f_names)