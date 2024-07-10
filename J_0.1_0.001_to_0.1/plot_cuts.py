import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
import sys

omega_c=float(sys.argv[1])
nu=float(sys.argv[2])
p=0.04
J=0.1


def func(x,a,b):
    return a*np.tanh(b*x)

if __name__=='__main__':
    L_arr=[12,16,32,48]
    omega_arr=np.linspace(0.001,0.1,18)
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
        chi=(m2_arr-m_arr**2)*L**2
        #plt.plot(omega_arr,m_arr,label=f"{L}")
        #plt.plot(omega_arr,bc,label=f"{L}")
        plt.plot(omega_c-omega_arr,chi,label=f"{L}")
        #plt.plot((omega_c-omega_arr)*L**(1/nu),bc,label=f"{L}")
    plt.legend()
    plt.grid()
    #plt.xlim(0.02,0.021)
    #plt.ylim(0.65,0.654)
    plt.xlabel('omega')
    plt.ylabel('bc')
    plt.show()
    #plt.savefig('bc_vs_omega.png')
    
