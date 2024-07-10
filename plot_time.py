import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
import sys

L=128#int(sys.argv[1])
p=0.04#float(sys.argv[2])
#i=int(sys.argv[3])
J=0.1


def func(x,a,b):
    return a*np.tanh(b*x)

if __name__=='__main__':
    omega_arr=np.linspace(0.018,0.028,20)
    #omega=0.008#omega_arr[i]    
    
    x=[1]
    for i in range(759):
        x.append(int(x[-1]*1.01+1))
    x=np.array(x)
    
    '''
    for omega in omega_arr:
        data=np.loadtxt(f'data_{J}_{p}_{omega}_{L}.txt',max_rows=3)
        m_arr=data[0]
        plt.plot(x,m_arr,label=f'omega={omega}')
    '''
    data=np.loadtxt(f'data_{J}_{p}_{omega_arr[7]}_{L}.txt',max_rows=3)
    m_arr=data[0]
    plt.plot(x,m_arr,label=f'omega={omega_arr[7]}')
    for i in range(759):
    	print(f'{x[i]} {m_arr[i]}')
    #popt,pcov=cf(func,x,m_arr)
    #a,b=popt[0],popt[1]
    
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('time')
    plt.ylabel('m')
    #plt. grid()
    plt.show()
    #plt.savefig('m_vs_t.png')
    #plt.title(f"L={L},p={p},omega={omega:.5f},J={J}")
    #plt.plot(x,func(x,a,b))
    #plt.show()
    #plt.savefig(f"L={L},p={p},omega={omega:.5f},J={J}.png")
