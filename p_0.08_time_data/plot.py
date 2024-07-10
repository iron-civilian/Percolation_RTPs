import numpy as np
import matplotlib.pyplot as plt
import sys

L=int(sys.argv[1])
p=float(sys.argv[2])
omega=float(sys.argv[3])

if __name__=="__main__":
    data=np.loadtxt(f"L{L}p{p}w{omega}.txt")
    data=data/(L*L)
    x=np.arange(1,L*L+1)
    y=data[1:]
    
    with open(f'dataL{L}p{p}w{omega}.text','a') as file:
        for i in range(len(x)):
            file.write(f"{x[i]} {y[i]}\n")
    
        
    '''
    plt.scatter(x,y,s=1)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    '''
