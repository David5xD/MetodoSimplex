import numpy as np
import scipy as sp

from scipy.optimize import linprog
# Librería scipy usando linprog

# PRIMER EJERCICIO (Cena e Insumos)

c=[8,6]
A_ub=[[-10,-5],[-6,-7]]
b_ub=[-40,-32]

x0_bounds=(0, None)
x1_bounds=(0, None)

res=linprog(c,A_ub,b_ub,bounds=(x0_bounds, x1_bounds),method='simplex')
print(res)
print("Valor Óptimo: ",res.fun,"       X: ",res.x)

print("===========================================")
# SEGUNDO EJERCICIO (Empresa)

c=[-21,-24,-36]
A_ub=[[1,1,1],[1,1,2],[2,3,5]]
b_ub=[400,500,1450]

res2=linprog(c,A_ub,b_ub,bounds=(0,None))
print(res2)
print("Valor Óptimo: ",res2.fun,"       X: ",res2.x)

print("===========================================")
# TERCER EJERCICIO

c=[2,-1]
A_ub=[[2,3],[1,1]]
b_ub=[10,6]

res3=linprog(c,A_ub,b_ub,bounds=(0,None))
print(res3)
print("Valor Óptimo: ",res3.fun,"       X: ",res3.x)
