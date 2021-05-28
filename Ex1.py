
#apenas para sistemas de 3 ordem

def arred(x):
    flag=False
    i=0
    while not flag:
        if x**2<0.01:
            x=x*10
            i-=1
        elif x**2>=1:
            x=x/10
            i+=1
        else:
            flag=True
    x=x*10**3
    xsalvo=x//1
    x=x%1
    if x*10>=5:
        x=int(xsalvo+1)
    else:
        x=int(xsalvo)
    x=x*10**(i-3)
    return x

def eliminacao():
    matriz=[] 
    for i in range(3):
        matriz.append([]) 
        for j in range(4):
            matriz[i].append('')
    for i in range(3):
        for j in range(4):
            print("digite o elemento A(", i+1,",",j+1,")")
            matriz[i][j]=float(input())

    a=matriz[1][0]/matriz[0][0]
    matriz[1][0]=arred(a)
    a=matriz[2][0]/matriz[0][0]
    matriz[2][0]=arred(a)
    print("1")
    ###
    a=matriz[1][0]*matriz[0][1]
    a=arred(a)
    a=matriz[1][1]-a
    matriz[1][1]=arred(a)#matriz[1][1]-matriz[1][0]*matriz[0][1]
    print("2")
    ###
    a=matriz[1][0]*matriz[0][2]
    a=arred(a)
    a=matriz[1][2]-a
    matriz[1][2]=arred(a)#matriz[1][2]-matriz[1][0]*matriz[0][2]
    print("3")###
    a=matriz[1][0]*matriz[0][3]
    a=arred(a)
    a=matriz[1][3]-a
    matriz[1][3]=arred(a)#matriz[1][3]-matriz[1][0]*matriz[0][3]
    print("4")###
    a=matriz[2][0]*matriz[0][1]
    a=arred(a)
    a=matriz[2][1]-a
    matriz[2][1]=arred(a)#matriz[2][1]-matriz[2][0]*matriz[0][1]
    print("5")###
    a=matriz[2][0]*matriz[0][2]
    a=arred(a)
    a=matriz[2][2]-a
    matriz[2][2]=arred(a)#matriz[2][2]-matriz[2][0]*matriz[0][2]
    print("6")###
    a=matriz[2][0]*matriz[0][3]
    a=arred(a)
    a=matriz[2][3]-a
    matriz[2][3]=arred(a)#matriz[2][3]-matriz[2][0]*matriz[0][3]
    print("7")###
    a=matriz[2][1]/matriz[1][1]
    matriz[2][1]=arred(a)#matriz[2][1]/matriz[1][1]
    print("8")###
    a=matriz[2][1]*matriz[1][2]
    a=arred(a)
    a=matriz[2][2]-a
    matriz[2][2]=arred(a)#matriz[2][2]-matriz[2][1]*matriz[1][2]
    print("9")###
    a=matriz[2][1]*matriz[1][3]
    a=arred(a)
    a=matriz[2][3]-a
    matriz[2][3]=arred(a)#matriz[2][3]-matriz[2][1]*matriz[1][3]
    a=matriz[2][3]/matriz[2][2]
    z=arred(a)#matriz[2][3]/matriz[2][2]
    a=matriz[1][2]*z
    a=arred(a)
    a=matriz[1][3]-a
    a=arred(a)
    a=a/matriz[1][1]
    y=arred(a)#(matriz[1][3]-matriz[1][2]*z)/matriz[1][1]
    a=matriz[0][2]*z
    a=arred(a)
    x=matriz[0][1]*y
    x=arred(x)
    a=matriz[0][3]-a-x
    a=arred(a)
    a=a/matriz[0][0]
    x=arred(a)#(matriz[0][3]-matriz[0][1]*y-matriz[0][2]*z)/matriz[0][0]

    #calculando a distancia
    mcalc=[x,y,z]
    mentrada=[]
    distancia=0
    for i in range (3):
        print("inserir números x",i+1)
        mentrada+=[float(input( ))]
    for i in range (3):
        d= mcalc[i]-mentrada[i]
        if d<0:
            d=d*(-1)
        if d>distancia:
            distancia=d
    
    print(x,y,z)
    print("distancia ||x-xbarra||: ", distancia)
    print("Determinante: ", matriz[0][0]*matriz[1][1]*matriz[2][2])

                    
                
    

#aplicação do programa
eliminacao()
