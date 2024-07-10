import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
import sys

L=48#int(sys.argv[1])
p=0.04#float(sys.argv[2])
#i=int(sys.argv[3])
beta=float(sys.argv[1])
omega_c=float(sys.argv[2])
J=0.1


def func(x,a,b):
    return a*x+b

if __name__=='__main__':
    omega_arr=np.linspace(0.015,0.03,18)
    #omega=0.008#omega_arr[i]    
    
    x=[1]
    for i in range(759):
        x.append(int(x[-1]*1.01+1))
    x=np.array(x)
    b_arr=[]
    for omega in omega_arr:
        data=np.loadtxt(f'data_{J}_{p}_{omega}_{L}.txt',max_rows=3)
        m_arr=data[0]
        #plt.plot(x,m_arr)
        popt,pcov=cf(func,x[550:],m_arr[550:])
        a,b=popt[0],popt[1]
        b_arr.append(b)
        #plt.plot(x,func(x,a,b),label=f'b={b},omega={omega:.3f}')
    plt.plot(-omega_arr+omega_c,b_arr,marker='o')
    for i in range(18):
    	print(f'{omega_arr[i]} {b_arr[i]}')
    #popt,pcov=cf(func,x,m_arr)
    #a,b=popt[0],popt[1]
    #popt,pcov=cf(func,np.log(-omega_arr[4:]+omega_c),np.log(b_arr[4:]))
    #a,b=popt[0],popt[1]
    
    #plt.plot(np.log(-omega_arr[4:]+omega_c),func(np.log(-omega_arr[4:]+omega_c),a,b))
    
    #plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    #plt.xlabel('time')
    #plt.ylabel('m')
    #plt. grid()
    plt.show()
    #plt.savefig('m_vs_t.png')
    #plt.title(f"L={L},p={p},omega={omega:.5f},J={J}")
    #plt.plot(x,func(x,a,b))
    #plt.show()
    #plt.savefig(f"L={L},p={p},omega={omega:.5f},J={J}.png")
