import numpy as np

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