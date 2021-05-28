#!/usr/bin/env python
# coding: utf-8

# In[167]:


import numpy as np

n= 3
a= np.array([[12,-8,3],[-3,5,2],[3,8,11]])
b = np.array([[-2],[-9],[-4]])
interaçoes = 100
beta = np.zeros(n)
erro = 0.001
x = np.zeros(3)
xold= np.array([[-7],[-3],[-9]])
print("a matriz A=", a,"b=",b,"x0=",xold)

#Critério de Sassenfeld#
for i in range (0,n):
    for j in range (0,i):
        beta[i]=beta[i]+np.abs(a[i,j])*beta[j]
    for j in range (i+1,n):
        beta[i]= beta[i] + np.abs(a[i,j])
    beta[i] = beta[i]/np.abs(a[i,i])
    print("beta", i+1,"=",beta[i])
betamax = np.max(beta)
print("o beta máximo=",betamax)
if betamax >= 1: 
    print("O critério de Sassenfeld nao foi satisfeito, a taxa é definida arbitrariamente")
    taxa = 1000
else:
    taxa = betamax/(1-betamax)
    print("a taxa é =",taxa)
for k in range (0,interaçoes):
    for i in range(0,n):
        x[i] = b[i]
        for j in range (0,i):
            x[i] = x[i]-a[i,j]*x[j]
        for j in range (i+1,n):
            x[i] = x[i] - a[i,j]*xold[j]
        x[i] = x[i]/a[i,i]
    error = taxa*(np.max(np.abs(x-xold)))
    print("após interaçao",k+1)
    print("x(", k+1,") = ",x)
    if error<erro:
        break
    xold= np.copy(x)
    
ax= np.matmul(a,x)
print("Ax = ",ax)


# In[ ]:





# In[ ]:




