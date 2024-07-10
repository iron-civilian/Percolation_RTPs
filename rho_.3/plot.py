import numpy as np
import matplotlib.pyplot as plt


if __name__=="__main__":
    x=np.arange(0.001,0.1,.002)
    y=np.linspace(0.001,0.5,100)
    X,Y=np.meshgrid(x,y)
    Z=np.zeros((100,50))
    data=np.loadtxt("5_4dataL32.txt",delimiter=',')
    
    for d in data:
        xx,yy,m=d[2],d[1],d[3]
        try:
            i=list(x).index(xx)
            j=list(y).index(yy)
            Z[j][i]=m
        except:
            continue
    plt.contourf(X, Y, Z,cmap='Blues')
    plt.xlabel(r'$\omega$',size='xx-large')
    plt.ylabel(r'p',size='xx-large')
    plt.yscale('log')
    plt.title(r'$\rho=0.3$')
    plt.colorbar()
    plt.show()
        
    
    
    
