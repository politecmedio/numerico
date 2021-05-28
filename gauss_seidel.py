import numpy                 as np

print("Método de Gauss-Seidel")

n=3
a=np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1, 4]])
b=np.ones(n)
eps = 1.0e-06
itmax = 2

print("Matriz A:")
print(np.matrix(a))
print('Matriz B:')
print(np.matrix(b))

beta=np.zeros(n)
x=np.zeros(n)
xold=np.zeros(n)

print("Verificando critério de Sassenfeld")
for i in range(0,n):
    for j in range(0,i):
        beta[i] = beta[i]+np.abs(a[i,j])*beta[j]
    for j in range(i+1,n):
        beta[i] = beta[i]+np.abs(a[i,j])
    beta[i] = beta[i] / np.abs(a[i,i])
    print("beta ",i+1," = ",beta[i])
betamax = np.max(beta)
if (betamax >= 1.):
    print("critério de Sassenfeld não satisfeito, taxa definida arbitrariamente")
    taxa = 10000
else:
    taxa=betamax/(1.-betamax)
print("betamax = ",betamax)
#
print("x (",0,")  = ", np.matrix(x))
print('')
for k in range(0,itmax):
    for i in range(0,n):
        x[i]=b[i]
        for j in range(0,i):
            x[i] = x[i]-a[i,j]*x[j]
        for j in range(i+1,n):
            x[i] = x[i]-a[i,j]*x[j]
        x[i] = x[i] / a[i,i]
    error = taxa*np.max(np.abs(x-xold))
    print("após iteração ",k+1, "erro estimado ",error)
    print("x (",k+1,")  = ", np.matrix(x))
    print('')
    if (error < eps):
        break
    xold = np.copy(x)
#
#    Verificando se temos a solução bem aproximada
#
ax = np.matmul(a,x)
print(" Ax = ",ax)
print("máximo do resíduo",np.max(np.abs(b-ax)))
#

