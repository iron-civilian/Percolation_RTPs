import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
import sys

L=int(sys.argv[1])
p=float(sys.argv[2])
i=int(sys.argv[3])
J=0.1


def func(x,a,b):
    return a*np.tanh(b*x)

if __name__=='__main__':
    omega_arr=np.linspace(0.001,0.1,18)
    omega=omega_arr[i]    
    data=np.loadtxt(f'data_{J}_{p}_{omega}_{L}.txt',max_rows=3)
    m_arr=data[0]
    x=[1]
    for i in range(759):
        x.append(int(x[-1]*1.01+1))
    x=np.array(x)
    
    
    
    #popt,pcov=cf(func,x,m_arr)
    #a,b=popt[0],popt[1]
    
    plt.plot(x,m_arr)
    plt.xscale('log')
    plt.xlabel('time')
    plt.ylabel('m')
    plt.title(f"L={L},p={p},omega={omega:.5f},J={J}")
    #plt.plot(x,func(x,a,b))
    plt.show()
    #plt.savefig(f"L={L},p={p},omega={omega:.5f},J={J}.png")
