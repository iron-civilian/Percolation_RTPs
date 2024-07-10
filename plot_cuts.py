import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
import sys


m=float(sys.argv[1])
c=float(sys.argv[2])

p=0.04
J=0.1




def func(x,m,c):
    return m*x+c



if __name__=='__main__':
    L_arr=[128]#[12,16,24,32,48]
    omega_arr=np.linspace(0.015,0.03,18)
    for L in L_arr:
        m_arr=[]
        m2_arr=[]
        m4_arr=[]
        for omega in omega_arr:
            m_arr.append(np.loadtxt(f'data_{J}_{p}_{omega}_{L}.txt',max_rows=3)[0][-1]/(L**2))  
            m2_arr.append(np.loadtxt(f'data_{J}_{p}_{omega}_{L}.txt',max_rows=3)[1][-1]/(L**4))    
            m4_arr.append(np.loadtxt(f'data_{J}_{p}_{omega}_{L}.txt',max_rows=3)[2][-1]/(L**8))
        m_arr=np.array(m_arr)
        m2_arr=np.array(m2_arr)
        m4_arr=np.array(m4_arr)
        bc=1-m4_arr/(3*m2_arr**2)
        
        #x_arr=np.log(omega_arr[7:]-0.021)
        #y_arr=-np.log(m_arr[7:])
        
        #popt,pcov=cf(func,x_arr,y_arr)
        #m,c=popt[0],popt[1]
        
        #plt.scatter(x_arr,y_arr,label=f'L={L}',color='black')
        #plt.plot(x_arr,func(x_arr,m,c),label=f'fit line',color='red')
        
        #plt.plot(omega_arr,m_arr,label=f'L={L}')
        plt.plot(omega_arr,bc,label=f'L={L}')
        #plt.plot((omega_arr-omega_c)*L**(1/nu),bc,label=f"{L}")
    plt.legend()
    plt.xlabel('omega')
    #plt.ylim(.65,.656)
    #plt.xlim(-.5,.5)
    plt.ylabel('bc')
    plt.grid()
    plt.show()
    #plt.savefig('bc_vs_omega.png')
    
